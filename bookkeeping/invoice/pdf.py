# -*- coding: UTF-8 -*-
from datetime import datetime

from django.conf import settings
from fpdf import FPDF

TOP_PAGE_MARGIN = 17.0
LEFT_PAGE_MARGIN = 17.0
RIGHT_PAGE_MARGIN = 192.0
START_TABLE_Y = 130.0
TABLE_ROW_HIGH = 5.0
COLUMN_1_WIDTH = 23  # date
COLUMN_2_WIDTH = 82  # description
COLUMN_3_WIDTH = 15  # count
COLUMN_4_WIDTH = 20  # amount
COLUMN_5_WIDTH = 20  # total
COLUMN_6_WIDTH = 15  # tax

COLUMNS = [(COLUMN_1_WIDTH, 'L'),
           (COLUMN_2_WIDTH, 'L'),
           (COLUMN_3_WIDTH, 'L'),
           (COLUMN_4_WIDTH, 'R'),
           (COLUMN_5_WIDTH, 'R'),
           (COLUMN_6_WIDTH, 'L')]


def invoice_to_PDF(client, order):
    pdf = FPDF()

    def text_fonts():
        pdf.set_font('Arial', '', 13.0)

    def add_row(column_data):
        """
        add a row to the pdf
        """
        cell_margin_left = 2
        cell_margin_right = 2

        row_y = pdf.get_y() if pdf.get_y() > START_TABLE_Y else START_TABLE_Y
        max_y = row_y  # max_y is used to check if multi cell is wrapping text and so uses more rows.

        next_x = LEFT_PAGE_MARGIN
        for i, column in enumerate(COLUMNS):
            width = column[0]
            align = column[1]
            pdf.set_xy(next_x+cell_margin_left, row_y)
            pdf.multi_cell(w=width-cell_margin_right, h=TABLE_ROW_HIGH, txt=column_data[i] if len(column_data) > i else '', align=align)
            max_y = max(max_y, pdf.get_y())  # keep track if multi cell wrapped text
            next_x += width

        pdf.set_y(max_y)

    def add_row_line():
        line_y = pdf.get_y() if pdf.get_y() > START_TABLE_Y else START_TABLE_Y - 2
        pdf.set_xy(LEFT_PAGE_MARGIN + 1, line_y)
        pdf.line(LEFT_PAGE_MARGIN, line_y+2, RIGHT_PAGE_MARGIN, line_y+2)
        pdf.set_y(line_y+5)

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
    pdf.set_font('helvetica', 'B', 15.0)
    pdf.write(6, 'Factuur {number}'.format(number='2014-0003'))
    text_fonts()
    pdf.set_xy(125, 75)
    pdf.write(6, 'Factuurdatum: {date}'.format(date=datetime.now().strftime("%d %B %Y")))
    pdf.set_xy(LEFT_PAGE_MARGIN, 85)
    pdf.write(5, 'Referentie: {reference}'.format(reference='Wens pak voor ...'))
    pdf.set_xy(LEFT_PAGE_MARGIN, 100)
    pdf.write(6, '{company}\n{street} {street_nr}\n{zip} {city}'.format(
        company=client.name, street=client.street, street_nr=client.street_nr,
        zip=client.zip, city=client.city
    ))


    ####
    # Article data
    ####
    pdf.set_font('Arial', '', 10.0)
    add_row_line()
    add_row(['Datum', 'Omschrijving', 'Aantal', 'Bedrag', 'Totaal', 'Btw'])
    add_row_line()
    add_row(['22-01-2014', 'jurk Princes Daisy (4,75 uur) lorum ipsum Doler latemsitu', '1', u'83,12', u'83,12', '21%'])
    add_row(['22-01-2014', 'jurk Princes Peach (5,75 uur)', '1', u'19293,45', u'19293,45', '21%'])
    add_row(['22-01-2014', 'jurk Princes Daisy (4,75 uur) lorum ipsum Doler latemsitu lorum ipsum Doler latemsitu lorum ipsum Doler latemsitu lorum ipsum Doler latemsitu', '1', u'83,12', u'83,12', '21%'])
    add_row(['22-01-2014', 'jurk Princes Peach (5,75 uur)', '1', u'19293,45', u'19293,45', '21%'])
    add_row(['22-01-2014', 'jurk Princes Peach (5,75 uur)', '1', u'19293,45', u'19293,45', '21%'])
    add_row_line()
    ####
    # draw table vertical lines
    ####
    line_y = pdf.get_y() - 3
    line_x = LEFT_PAGE_MARGIN
    first = True
    for column in COLUMNS:
        if first:
            pdf.line(line_x, START_TABLE_Y, line_x, line_y)  # vertical line in front of table
            first = False

        line_x += column[0]
        pdf.line(line_x, START_TABLE_Y, line_x, line_y)  # vertical line after column

    add_row(['', 'Subtotaal excl. btw', '', '', '19293,45', ''])
    add_row(['', 'Btw', '', '', '1783,34', ''])
    add_row_line()
    pdf.set_font('Arial', 'B', 10.0)
    add_row(['', 'Totaal', '', '', '21783,34', ''])


    table_bottom = pdf.get_y() + 2
    pdf.line(LEFT_PAGE_MARGIN, table_bottom, RIGHT_PAGE_MARGIN, table_bottom)  # bottom horizontal line



    pdf.output('/tmp/invoice.pdf', 'F')
