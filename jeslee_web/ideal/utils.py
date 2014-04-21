from django.conf import settings
import hashlib
import math

__author__ = 'ceasaro'


def calculate_hash(order, valid_util):

    string_to_encode = settings.IDEAL_HASH_KEY         # iDEAL hash key
    string_to_encode += settings.IDEAL_MERCHANT_ID     # acceptant ID / merchant ID
    string_to_encode += '0'                            # sub_id
    amount = amount_in_cents(order)
    string_to_encode += str(amount)                    # total amount in cents
    string_to_encode += order.number                   # purchase ID
    string_to_encode += settings.IDEAL_PAYMENT_TYPE    # payment type

    string_to_encode += valid_util                     # valid_util

    # TODO: split items in multiple orders?? for now use the order as one
    string_to_encode += str(1)                         # item number
    string_to_encode += order.get_name()               # order description
    string_to_encode += str(1)                         # order quantity
    string_to_encode += str(amount)                    # order price

    string_to_encode = "".join(string_to_encode.split())
    # return string_to_encode
    sha1 = hashlib.sha1()
    sha1.update(string_to_encode)
    return sha1.hexdigest()


# def create_description(order):
#     return "Jeslee order. e-mail:{email}, name:{name}".format(
#         email=order.customer_email,
#         name=order.get_name())

def amount_in_cents(order):
    return  int(math.ceil(order.price * 100))
