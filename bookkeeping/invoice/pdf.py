# -*- coding: UTF-8 -*-
from datetime import datetime, timedelta
import locale

from django.conf import settings
from fpdf import FPDF


PAY_INVOICE_WITHIN_DAYS = 14

TOP_PAGE_MARGIN = 17.0
LEFT_PAGE_MARGIN = 17.0
RIGHT_PAGE_MARGIN = 192.0
START_TABLE_Y = 130.0
PAGE_BOTTOM_Y = 265
TABLE_ROW_HIGH = 5.0
COLUMN_1_WIDTH = 30  # code
COLUMN_2_WIDTH = 72  # description
COLUMN_3_WIDTH = 8   # count
COLUMN_4_WIDTH = 25  # amount
COLUMN_5_WIDTH = 25  # total
COLUMN_6_WIDTH = 15  # tax

COLUMNS = [(COLUMN_1_WIDTH, 'L'),
           (COLUMN_2_WIDTH, 'L'),
           (COLUMN_3_WIDTH, 'L'),
           (COLUMN_4_WIDTH, 'R'),
           (COLUMN_5_WIDTH, 'R'),
           (COLUMN_6_WIDTH, 'L')]


def to_currency(float):
    currency = locale.currency(float, grouping=True).strip()
    if ' ' in currency:
        tuple = currency.split(' ', 1)
        return "{0} {1}".format(tuple[0], tuple[1].replace(' ', '.'))
    return currency


def invoice_to_PDF(order, client, filename=None):
    """
    creates and pdf invoice of the order, and returns the pfd as a string buffer.
    @order: the order used to create a invoice
    @client: if specified this data is used for the client address, otherwise the address is taken from the order
    @filename: if specified the pdf is written to disk with the given filename,
               filename can contains a complete path
    """
    pdf = FPDF()
    pdf.add_font('DejaVu', '', fname='{0}/fonts/ttf-dejavu/DejaVuSerif.ttf'.format(settings.STATIC_ROOT), uni=True)
    pdf.add_font('DejaVu', 'B', fname='{0}/fonts/ttf-dejavu/DejaVuSerif-Bold.ttf'.format(settings.STATIC_ROOT), uni=True)
    pdf.add_font('DejaVu', 'I', fname='{0}/fonts/ttf-dejavu/DejaVuSerif-Italic.ttf'.format(settings.STATIC_ROOT), uni=True)
    pdf.add_font('DejaVu', 'BI', fname='{0}/fonts/ttf-dejavu/DejaVuSerif-BoldItalic.ttf'.format(settings.STATIC_ROOT), uni=True)

    def check_for_new_page():
        if pdf.get_y() > PAGE_BOTTOM_Y:
            pdf.add_page()

    def text_fonts():
        pdf.set_font('DejaVu', '', 11.0)

    def add_row(column_data, columns=COLUMNS, border=0):
        """
        add a row to the pdf
        """
        cell_margin_left = 2
        cell_margin_right = 2

        check_for_new_page()
        last_y = START_TABLE_Y if pdf.page_no() == 1 else TOP_PAGE_MARGIN
        row_y = pdf.get_y() if pdf.get_y() > last_y else last_y
        max_y = row_y  # max_y is used to check if multi cell is wrapping text and so uses more rows.

        next_x = LEFT_PAGE_MARGIN
        for i, column in enumerate(columns):
            width = column[0]
            align = column[1]
            pdf.set_xy(next_x+cell_margin_left, row_y)
            pdf.multi_cell(w=width-cell_margin_right,
                           h=TABLE_ROW_HIGH,
                           txt=column_data[i] if len(column_data) > i else '', align=align, border=border)
            max_y = max(max_y, pdf.get_y())  # keep track if multi cell wrapped text
            next_x += width

        pdf.set_y(max_y)

    def add_row_line():
        last_y = START_TABLE_Y if pdf.page_no() == 1 else TOP_PAGE_MARGIN
        line_y = pdf.get_y() if pdf.get_y() > last_y else last_y - 2
        pdf.set_xy(LEFT_PAGE_MARGIN + 1, line_y)
        pdf.line(LEFT_PAGE_MARGIN, line_y+2, RIGHT_PAGE_MARGIN, line_y+2)
        pdf.set_y(line_y+5)

    def draw_vertical_lines_around_columns(columns = COLUMNS, top_y=TOP_PAGE_MARGIN, bottom_y=PAGE_BOTTOM_Y):
        ####
        # draw table vertical lines
        ####
        line_y = pdf.get_y() - 3
        line_x = LEFT_PAGE_MARGIN
        first = True
        for column in columns:
            if first:
                pdf.line(line_x, START_TABLE_Y, line_x, line_y)  # vertical line in front of table
                first = False

            line_x += column[0]
            pdf.line(line_x, START_TABLE_Y, line_x, line_y)  # vertical line after column

    pdf.add_page()
    text_fonts()

    ####
    # Header: logo and company info
    ####
    pdf.image('{0}/gfx/logos/logo_jeslee.jpg'.format(settings.STATIC_ROOT), 20.0, TOP_PAGE_MARGIN, link='', type='', w=79.5, h=33.0)
    pdf.set_xy(125.0, TOP_PAGE_MARGIN)
    # pdf.set_font('arial', 'B', 13.0)
    pdf.set_left_margin(125.0)
    pdf.write(6, '{company}\n{street}\n{zip} {city}\n{email}\nKvk: {kvk}\nBTW: {btw}'.format(
        company=settings.COMPANY['business_name'],
        street=settings.COMPANY['street'], zip=settings.COMPANY['zip'], city=settings.COMPANY['city'],
        email=settings.COMPANY['email'], kvk=settings.COMPANY['kvk_nr'], btw=settings.COMPANY['btw_nr']
    ))

    ####
    # Invoice data
    ####
    pdf.set_xy(LEFT_PAGE_MARGIN, 75)
    pdf.set_left_margin(LEFT_PAGE_MARGIN)
    pdf.set_font('DejaVu', 'B', 14.0)
    pdf.write(6, 'Factuur {number}'.format(number=order.number))
    text_fonts()
    pdf.set_xy(125, 75)
    pdf.write(6, 'Factuurdatum: {date}'.format(date=datetime.now().strftime("%d %B %Y")))
    pdf.set_xy(LEFT_PAGE_MARGIN, 85)
    pdf.write(5, 'Referentie: {reference}'.format(reference=order.message if order.message else 'Uw bestelling bij Jeslee'))
    pdf.set_xy(LEFT_PAGE_MARGIN, 100)
    name = order.invoice_company_name \
        if order.invoice_company_name \
        else "{0} {1}".format(order.invoice_firstname, order.invoice_lastname)
    address = "{0} {1}".format(order.invoice_line1, order.invoice_line2)
    pdf.write(6, '{name}\n{address}\n{zip} {city}'.format(
        name=name.strip(), address=address.strip(),
        zip=order.invoice_code, city=order.invoice_city
    ))


    ####
    # Article data
    ####
    pdf.set_font('DejaVu', '', 9.0)
    add_row_line()
    add_row(['Artikelcode', 'Omschrijving', '#', 'Bedrag ¹', 'Totaal ¹', 'Btw'])
    add_row_line()
    for item in order.items.all():
        code = ''
        description = ''
        if item.product:
            code = item.product.sku
            description = item.product.description if item.product.description else item.product.name
            str(item.product.tax if item.product.tax else '')
        add_row([code,
                 description,
                 "{:.0f}".format(item.product_amount) if item.product_amount else 0,
                 to_currency(item.product_price_gross),
                 to_currency(item.price_gross),
                 str(item.product.tax if item.product and item.product.tax else "")])

    add_row_line()

    columns_below_items = [(COLUMN_1_WIDTH + COLUMN_2_WIDTH + COLUMN_3_WIDTH+COLUMN_4_WIDTH , 'R'),
                           (COLUMN_5_WIDTH, 'R'),
          (COLUMN_6_WIDTH, 'L')]
    add_row(['Subtotaal ²', to_currency(order.price-order.tax)], columns=columns_below_items)
    add_row(['Btw.', to_currency(order.tax)], columns=columns_below_items)
    add_row_line()
    pdf.set_font('DejaVu', 'B', 10.0)
    add_row(['Totaal', to_currency(order.price)], columns=columns_below_items)


    table_bottom = pdf.get_y() + 2
    pdf.line(LEFT_PAGE_MARGIN, table_bottom, RIGHT_PAGE_MARGIN, table_bottom)  # bottom horizontal line


    pdf.set_font('DejaVu', '', 10.0)
    pdf.set_xy(LEFT_PAGE_MARGIN, PAGE_BOTTOM_Y-18)
    pay_date = datetime.now() + timedelta(PAY_INVOICE_WITHIN_DAYS)
    pdf.write(5, 'We verzoeken u vriendelijk het bovenstaande bedrag van {order_price} voor '
                 '{pay_date} te voldoen op onze bankrekening onder vermelding van het '
                 'factuurnummer {invoice_number}.'.
              format(order_price=to_currency(order.price),
                     pay_date=pay_date.strftime("%d %B %Y"),
                     invoice_number=order.number))
    pdf.set_xy(LEFT_PAGE_MARGIN, PAGE_BOTTOM_Y-6)
    pdf.write(5, 'Voor vragen kunt u contact opnemen per e­mail.')

    pdf.set_draw_color(80)
    pdf.set_text_color(80)
    pdf.line(LEFT_PAGE_MARGIN, PAGE_BOTTOM_Y, RIGHT_PAGE_MARGIN, PAGE_BOTTOM_Y)  # bottom horizontal line
    pdf.set_xy(LEFT_PAGE_MARGIN+5, PAGE_BOTTOM_Y+2)
    pdf.set_font('DejaVu', '', 8.0)
    pdf.write(4, '¹) Bedragen zijn inclusief btw.')
    pdf.set_xy(LEFT_PAGE_MARGIN+5, PAGE_BOTTOM_Y+6)
    pdf.write(4, '²) Bedrag is exclusief btw.')
    if filename:
        pdf.output(filename, 'F')
    return pdf.output('invoice.pdf', 'S')
