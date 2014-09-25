__author__ = 'ceasaro'

#
# company settings
#
COMPANY = {
    'name': 'Jeslee',
    'business_name': 'Jeslee',
    'street': 'Hoofdstraat 51',
    'zip': '9635 AT',
    'city': 'Noordbroek',
    'country': 'Nederland',
    'email': 'info@jeslee.com',
    'mobile': '06 - 15 94 80 90',
    'bank_account': 'NL51 INGB 0657 7504 76',
    'kvk_nr': '01131652',
    'btw_nr': 'NL238283057b01',
}


#
# iDEAL settings (TEST environment, live settings in production.py)
#
IDEAL_PAYMENT_URL = 'https://idealtest.secure-ing.com/ideal/mpiPayInitIng.do'
IDEAL_MERCHANT_ID = '005081894'
IDEAL_HASH_KEY = 'gxfE9kiasIyZ2yZU'
IDEAL_DEFAULT_SUB_ID = '0'
IDEAL_PAYMENT_TYPE = 'ideal'

