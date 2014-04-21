# Create your views here.
from abc import abstractmethod
from datetime import datetime, timedelta
from django.conf import settings
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView
from lfs.order.models import Order
from jeslee_web.ideal.utils import calculate_hash, amount_in_cents


class TestOrder(Order):

    def __init__(self, *args, **kwargs):
        self.test_name = ''
        super(TestOrder, self).__init__(*args, **kwargs)

    def get_name(self):
        return self.test_name

    def set_name(self, test_name):
        self.test_name = test_name


class IdealIngTestCase(TemplateView):
    context_object_name = 'order'

    def get_context_data(self, **kwargs):
        order = self.get_order()
        context_data = super(IdealIngTestCase, self).get_context_data(**kwargs)
        context_data[self.context_object_name] = order
        context_data['merchant_id'] = settings.IDEAL_MERCHANT_ID
        context_data['sub_id'] = settings.IDEAL_DEFAULT_SUB_ID
        context_data['amount_in_cents'] = amount_in_cents(order)
        context_data['currency'] = 'EUR'
        context_data['description'] = 'order from {domain}'.format(domain=Site.objects.get_current())
        valid_util_timestamp = datetime.now() + timedelta(minutes=15)
        valid_util = valid_util_timestamp.strftime('%Y-%m-%dT%H:%M:%S:%fZ')
        context_data['hash_key'] = settings.IDEAL_HASH_KEY
        context_data['hash'] = calculate_hash(order, valid_util=valid_util)
        context_data['payment_type'] = settings.IDEAL_PAYMENT_TYPE
        context_data['valid_util'] = valid_util

        context_data['success_url'] = reverse('ideal-success')
        context_data['cancel_url'] = reverse('ideal-cancel')
        context_data['error_url'] = reverse('ideal-error')
        return context_data

    @staticmethod
    @abstractmethod
    def get_order():
        """
        Abstract method need to be overwritten by it's subclasses.
        """
        return TestOrder()


class IngTest1View(IdealIngTestCase):

    def get_order(self):
        order = TestOrder()
        order.price = 1.00
        order.test_name = 'Test case 1 Success'
        order.number = 'test_case_1'
        order.message = 'By sending a payment transaction with an amount of 1 EURO the returned issuer state is a success'
        return order


class IngTest2View(IdealIngTestCase):

    def get_order(self):
        order = TestOrder()
        order.price = 2.00
        order.test_name = 'Test case 2: Cancelled'
        order.number = 'test_case_2'
        order.message = 'By sending a payment transaction with an amount of 2 EURO the returned issuer state is a cancelled'
        return order


class IngTest3View(IdealIngTestCase):

    def get_order(self):
        order = TestOrder()
        order.price = 3.00
        order.test_name = 'Test case 3: Expired'
        order.number = 'test_case_3'
        order.message = 'By sending a payment transaction with an amount of 3 EURO the returned issuer state is a expired'
        return order


class IngTest4View(IdealIngTestCase):

    def get_order(self):
        order = TestOrder()
        order.price = 4.00
        order.test_name = 'Test case 4: Open'
        order.number = 'test_case_4'
        order.message = 'By sending a payment transaction with an amount of 4 EURO the returned issuer state is a open'
        return order


class IngTest5View(IdealIngTestCase):

    def get_order(self):
        order = TestOrder()
        order.price = 5.00
        order.test_name = 'Test case 5: Failure'
        order.number = 'test_case_5'
        order.message = 'By sending a payment transaction with an amount of 5 EURO the returned issuer state is a failure'
        return order


class IngTest6View(IdealIngTestCase):

    def get_order(self):
        order = TestOrder()
        order.price = 6.00
        order.test_name = 'Test case 6: Directory Request'
        order.number = 'test_case_6'
        order.message = 'Sending a successful directory request'
        return order


class IngTest7View(IdealIngTestCase):

    def get_order(self):
        order = TestOrder()
        order.price = 7.00
        order.test_name = 'Test case 7: Format Error'
        order.number = 'test_case_7'
        order.message = 'Format error by sending a payment transaction with 7 EURO'
        return order