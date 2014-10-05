__author__ = 'ceasaro'


def get_payment_quarter_data(payment_list):
    """
    return a dictionary with the total amount and taxes of the payment_list as well of the total amount and taxes
    of every quarter.

     dict returned is:
    {
        'total': 0,         # total of all amounts
        'total_tax': 0,     # total of all tax
        'q1_total': 0,      # total of all amounts in quarter 1 (jan, feb, mar)
        'q1_total_tax': 0,  # total of all tax in quarter 1 (jan, feb, mar)
        'q2_total': 0,      # total of all amounts in quarter 2 (apr, may, jun)
        'q2_total_tax': 0,  # total of all tax in quarter 2 (apr, may, jun)
        'q3_total': 0,      # total of all amounts in quarter 3 (jul, aug, sep)
        'q3_total_tax': 0,  # total of all tax in quarter 3 (jul, aug, sep)
        'q4_total': 0,      # total of all amounts in quarter 4 (okt, nov, dec)
        'q4_total_tax': 0,  # total of all tax in quarter 4 (okt, nov, dec)
    }
    """
    payment_quarter_data = {
        'total': 0,  # total of all amounts
        'total_tax': 0,  # total of all tax
        'q1_total': 0,  # total of all amounts in quarter 1 (jan, feb, mar)
        'q1_total_tax': 0,  # total of all tax in quarter 1 (jan, feb, mar)
        'q2_total': 0,  # total of all amounts in quarter 2 (apr, may, jun)
        'q2_total_tax': 0,  # total of all tax in quarter 2 (apr, may, jun)
        'q3_total': 0,  # total of all amounts in quarter 3 (jul, aug, sep)
        'q3_total_tax': 0,  # total of all tax in quarter 3 (jul, aug, sep)
        'q4_total': 0,  # total of all amounts in quarter 4 (okt, nov, dec)
        'q4_total_tax': 0,  # total of all tax in quarter 4 (okt, nov, dec)
    }
    for payment in payment_list:
        payment_quarter_data['total'] += payment.amount
        payment_quarter_data['total_tax'] += payment.tax
        if payment.pay_date.month in (1, 2, 3):  # quarter 1 (jan, feb, mar)
            payment_quarter_data['q1_total'] += payment.amount
            payment_quarter_data['q1_total_tax'] += payment.tax
        if payment.pay_date.month in (4, 5, 6):  # quarter 2 (apr, may, jun)
            payment_quarter_data['q2_total'] += payment.amount
            payment_quarter_data['q2_total_tax'] += payment.tax
        if payment.pay_date.month in (7, 8, 9):  # quarter 3 (jul, aug, sep)
            payment_quarter_data['q3_total'] += payment.amount
            payment_quarter_data['q3_total_tax'] += payment.tax
        if payment.pay_date.month in (10, 11, 12):  # quarter 4 (okt, nov, dec)
            payment_quarter_data['q4_total'] += payment.amount
            payment_quarter_data['q4_total_tax'] += payment.tax
    return payment_quarter_data

