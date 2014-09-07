from django.contrib.admin.views.decorators import staff_member_required
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, CreateView, UpdateView, DetailView
from lfs.order.models import Order

from bookkeeping.bookkeeping_core.models import Client
from bookkeeping.client.forms import ClientForm


__author__ = 'ceasaro'


class ClientOverview(TemplateView):

    def get_context_data(self, **kwargs):
        context = super(ClientOverview, self).get_context_data(**kwargs)
        context.update({'clients': Client.objects.all()})
        return context


class ClientDetailView(DetailView):
    model = Client
    context_object_name = 'client'

    def get_context_data(self, **kwargs):
        context_data = super(ClientDetailView, self).get_context_data(**kwargs)
        client = context_data[self.context_object_name]
        context_data.update({
            'orders': Order.objects.filter(user=client.user)
        })
        return context_data

    def get_object(self, queryset=None):
        return super(ClientDetailView, self).get_object(queryset)


class ClientCreateView(CreateView):
    form_class = ClientForm

    @method_decorator(staff_member_required)
    def dispatch(self, *args, **kwargs):
        return super(ClientCreateView, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse('client_home')


class ClientUpdateView(UpdateView):
    form_class = ClientForm
    model = Client

    @method_decorator(staff_member_required)
    def dispatch(self, *args, **kwargs):
        return super(ClientUpdateView, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse('client_home')
