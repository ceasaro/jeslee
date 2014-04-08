from django.conf import settings
import hashlib
import math

__author__ = 'ceasaro'


def calculate_hash(order, valid_util, order_quantity=1):

    sha1 = hashlib.sha1()
    sha1.update(settings.IDEAL_HASH_KEY)        # iDEAL hash key
    sha1.update(settings.IDEAL_MERCHANT_ID)     # acceptant ID / merchant ID
    sha1.update('0')                            # sub_id
    sha1.update(str(amount_in_cents(order)))    # total amount in cents
    sha1.update(order.number)                   # purchase ID
    sha1.update(settings.IDEAL_PAYMENT_TYPE)    # payment type

    sha1.update(valid_util)                     # valid_util

    # TODO: split items in multiple orders?? for now use the order as one
    sha1.update(order.number)                   # order number
    sha1.update(create_description(order))      # order description
    sha1.update(str(order_quantity))            # order quantity
    sha1.update(str(amount_in_cents))           # order price
    return sha1.hexdigest()


def create_description(order):
    return "Jeslee order. e-mail:{email}, name:{name}".format(
        email=order.customer_email,
        name=order.get_name())

def amount_in_cents(order):
    return  int(math.ceil(order.price * 100))
