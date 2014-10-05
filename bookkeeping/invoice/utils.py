from collections import Counter, OrderedDict

from django.conf import settings
from django.utils.text import slugify
from lfs.catalog.models import Product
from lfs.core.models import Country
from lfs.core.utils import import_symbol
from lfs.order.models import OrderItem, Order

from jeslee_web.lfs_patch.order.utils import tax_per_percentage


__author__ = 'ceasaro'


def add_order_item(order, data):
    article_price = float(data['article_price'])
    article_count = float(data['article_count'])
    item_price = article_price * article_count
    tax = data['tax']
    item_tax = item_price * tax.rate / 100
    try:
        product = Product.objects.get(name=data['name'])
    except Product.DoesNotExist:
        product = Product.objects.create(
            name=data['name'],
            slug=slugify(data['name']),
            sku=data['article_code'],
            description=data['description'],
            tax=tax,
        )
    item = OrderItem.objects.create(
        order=order,
        price_gross=item_price,
        price_net=item_price * (100 - tax.rate) / 100,
        tax=item_tax,
        product=product,
        product_sku=data['article_code'],
        product_amount=article_count,
        product_name=data['name'],
        product_price_net=article_price * (100-tax.rate) / 100,
        product_price_gross=article_price,
        product_tax=article_price * tax.rate / 100,
    )
    order.price += item_price
    order.tax += item_tax
    return item, order


def create_order(form_data, request):
    client = form_data['client']
    order = Order.objects.create(
        user=client.user,
        invoice_line2=form_data['reference'],
        message=form_data['message'],

        session=request.session.session_key,
        # tax=form_data['product_price_gross'] * form_data['product_tax'],

        customer_firstname=client.name,
        customer_lastname='',
        customer_email=client.user.email,

        invoice_firstname=client.name,
        invoice_lastname='',
        invoice_company_name=client.name,
        invoice_line1='{street} {nr}'.format(street=client.street, nr=client.street_nr),
        # invoice_line2='', used for the invoice reference
        invoice_city=client.city,
        invoice_state='',
        invoice_code=client.zip,
        invoice_country=Country.objects.get(code='nl'),
        invoice_phone='',

    )
    ong = import_symbol(settings.LFS_ORDER_NUMBER_GENERATOR)
    try:
        order_numbers = ong.objects.get(id="order_number")
    except ong.DoesNotExist:
        order_numbers = ong.objects.create(id="order_number")

    try:
        order_numbers.init(request, order)
    except AttributeError:
        pass

    order.number = order_numbers.get_next()
    return order


def get_invoice_quarter_data(order_list):
    """
    return a dictionary with the total price and taxes of the order_list as well of the total price and taxes
    of every quarter.

    dict returned is:
    {
        'total': 0,                             # total of all prices
        'total_taxes': {'6%', 10, '21%', 34},   # total of all taxes
        'q1_total': 0,                          # total of all prices in quarter 1 (jan, feb, mar)
        'q1_total_tax': {'6%', 0, '21%', 4},    # total of all tax in quarter 1 (jan, feb, mar)
        'q2_total': 0,                          # total of all prices in quarter 2 (apr, may, jun)
        'q2_total_tax': {'6%', 2, '21%', 10},   # total of all tax in quarter 2 (apr, may, jun)
        'q3_total': 0,                          # total of all prices in quarter 3 (jul, aug, sep)
        'q3_total_tax': {'6%', 2, '21%', 4},    # total of all tax in quarter 3 (jul, aug, sep)
        'q4_total': 0,                          # total of all prices in quarter 4 (okt, nov, dec)
        'q4_total_tax': {'6%', 8, '21%', 16},   # total of all tax in quarter 4 (okt, nov, dec)
    }
    """
    invoice_quarter_data = {
        'total': 0,                     # total of all prices
        'total_taxes': Counter({}),     # total of all taxes
        'q1_total': 0,                  # total of all prices in quarter 1 (jan, feb, mar)
        'q1_total_taxes': Counter({}),    # total of all tax in quarter 1 (jan, feb, mar)
        'q2_total': 0,                  # total of all prices in quarter 2 (apr, may, jun)
        'q2_total_taxes': Counter({}),    # total of all tax in quarter 2 (apr, may, jun)
        'q3_total': 0,                  # total of all prices in quarter 3 (jul, aug, sep)
        'q3_total_taxes': Counter({}),    # total of all tax in quarter 3 (jul, aug, sep)
        'q4_total': 0,                  # total of all prices in quarter 4 (okt, nov, dec)
        'q4_total_taxes': Counter({}),    # total of all tax in quarter 4 (okt, nov, dec)
    }
    for order in order_list:
        taxes = Counter(tax_per_percentage(order))
        invoice_quarter_data['total'] += order.price
        invoice_quarter_data['total_taxes'] += taxes
        if order.created.month in (1, 2, 3):  # quarter 1 (jan, feb, mar)
            invoice_quarter_data['q1_total'] += order.price
            invoice_quarter_data['q1_total_taxes'] += taxes
        if order.created.month in (4, 5, 6):  # quarter 2 (apr, may, jun)
            invoice_quarter_data['q2_total'] += order.price
            invoice_quarter_data['q2_total_taxes'] += taxes
        if order.created.month in (7, 8, 9):  # quarter 3 (jul, aug, sep)
            invoice_quarter_data['q3_total'] += order.price
            invoice_quarter_data['q3_total_taxes'] += taxes
        if order.created.month in (10, 11, 12):  # quarter 4 (okt, nov, dec)
            invoice_quarter_data['q4_total'] += order.price
            invoice_quarter_data['q4_total_taxes'] += taxes

    # convert all Counters to plain dicts
    total_taxes = dict(invoice_quarter_data['total_taxes'])
    order_total_taxes = OrderedDict(sorted(total_taxes.items()))
    invoice_quarter_data['total_taxes'] = order_total_taxes
    invoice_quarter_data['q1_total_taxes'] = dict(invoice_quarter_data['q1_total_taxes'])
    invoice_quarter_data['q2_total_taxes'] = dict(invoice_quarter_data['q2_total_taxes'])
    invoice_quarter_data['q3_total_taxes'] = dict(invoice_quarter_data['q3_total_taxes'])
    invoice_quarter_data['q4_total_taxes'] = dict(invoice_quarter_data['q4_total_taxes'])
    return invoice_quarter_data

