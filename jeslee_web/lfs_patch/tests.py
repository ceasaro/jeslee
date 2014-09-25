from datetime import datetime

from django.test import TransactionTestCase
from lfs.order.models import Order, OrderItem
from lfs.order.settings import SUBMITTED

from jeslee_web.lfs_patch.order.utils import tax_per_percentage


__author__ = 'ceasaro'


class OrderUtilsTest(TransactionTestCase):


    @classmethod
    def setUpClass(cls):
        super(OrderUtilsTest, cls).setUpClass()

    def add_order_item(self, order, tax_percentage, price_gross):

        price_net = price_gross / tax_percentage if tax_percentage > 0 else price_gross
        OrderItem.objects.create(order=order,
                                 price_net=price_net,
                                 price_gross=price_gross,
                                 tax=price_gross*tax_percentage)

    def test_tax_per_percentage(self):
        order = Order.objects.create(number='n1',
                                     created=datetime.now(),
                                     state=SUBMITTED,
                                     customer_firstname='testcees',
                                     customer_lastname='vw',
                                     customer_email='niet@bekend.nu')

        tax_21 = 0.21
        tax_6 = 0.06
        tax_0 = 0.0
        self.add_order_item(order, tax_21, 100)
        self.add_order_item(order, tax_21, 120)
        self.add_order_item(order, tax_6, 10)
        self.add_order_item(order, tax_6, 50)
        self.add_order_item(order, tax_0, 350)
        self.add_order_item(order, tax_0, 15)

        taxes = tax_per_percentage(order)

        self.assertEquals(len(taxes), 2, "only two taxes should be present, cause the 0 tax should be eliminated")
        self.assertEquals(taxes[21], 46.20)
        self.assertEquals(taxes[6], 3.60)