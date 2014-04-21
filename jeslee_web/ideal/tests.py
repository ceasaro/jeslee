"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
import hashlib
from django.conf import settings

from django.test import SimpleTestCase
from lfs.order.models import Order
from mock import Mock
from jeslee_web.ideal.utils import calculate_hash


class SimpleTest(SimpleTestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)


class IDEALTest(SimpleTestCase):

    def setUp(self):
        # MOCK iDEAL hash key
        self.ori_ideal_hash_key = settings.IDEAL_HASH_KEY
        settings.IDEAL_HASH_KEY = 'Password'
        # acceptant ID / merchant ID
        self.ori_ideal_merchant_id = settings.IDEAL_MERCHANT_ID
        settings.IDEAL_MERCHANT_ID = '123456789'
        # payment type
        self.ori_ideal_payment_type = settings.IDEAL_PAYMENT_TYPE
        settings.IDEAL_PAYMENT_TYPE = 'ideal'

    def test_calc_hash(self):
        order = Order()
        order.price = 875.18
        order.customer_email = 'ceesvw@gmail.com'
        order.get_name = Mock(return_value='Order omschrijving')
        order.number = '3418683'
        hash = calculate_hash(order=order, valid_util='2014-04-21T12:57:04Z')
        self.assertEqual("b4c2204290b720f1e1dd57cf2bdf7cddecbf2c07", hash)

    def tearDown(self):
        settings.IDEAL_HASH_KEY = self.ori_ideal_hash_key
        settings.IDEAL_MERCHANT_ID = self.ori_ideal_merchant_id
        settings.IDEAL_PAYMENT_TYPE = self.ori_ideal_payment_type
