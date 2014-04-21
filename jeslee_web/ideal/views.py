# Create your views here.
from datetime import datetime, timedelta
from django.conf import settings
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django.views.generic import DetailView
from lfs.order.models import Order
from jeslee_web.ideal.utils import calculate_hash, amount_in_cents


class IdealOrder(DetailView):
    model = Order
    context_object_name = 'order'

    def get_context_data(self, **kwargs):
        context_data = super(IdealOrder, self).get_context_data(**kwargs)
        context_data['merchant_id'] = settings.IDEAL_MERCHANT_ID
        context_data['sub_id'] = settings.IDEAL_DEFAULT_SUB_ID
        context_data['amount_in_cents'] = amount_in_cents(self.object)
        context_data['currency'] = 'EUR'
        context_data['description'] = 'order from {domain}'.format(domain=Site.objects.get_current())
        valid_util_timestamp = datetime.now() + timedelta(minutes=15)
        valid_util = valid_util_timestamp.strftime('%Y-%m-%dT%H:%M:%S:%fZ')
        context_data['hash_key'] = settings.IDEAL_HASH_KEY
        context_data['hash'] = calculate_hash(self.object, valid_util=valid_util)
        context_data['payment_type'] = settings.IDEAL_PAYMENT_TYPE
        context_data['valid_util'] = valid_util

        context_data['success_url'] = reverse('ideal-success')
        context_data['cancel_url'] = reverse('ideal-cancel')
        context_data['error_url'] = reverse('ideal-error')
        return context_data


