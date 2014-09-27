__author__ = 'ceasaro'


def tax_per_percentage(order):
    """
    Returns a dictionary with the accumulated tax amount per percentage of each order item
    e.g.
    {'21.0%': 34.23,
     '6.0%': 23.4}
    """
    taxes = {}
    for item in order.items.all():
        if item.tax > 0:
            tax_percentage = int(round(item.tax / item.price_gross * 100))
            if tax_percentage in taxes.keys():
                taxes[tax_percentage] += item.tax
            else:
                taxes[tax_percentage] = item.tax
    return taxes