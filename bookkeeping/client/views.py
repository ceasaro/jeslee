from django.contrib.admin.views.decorators import staff_member_required
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, CreateView, UpdateView

from bookkeeping.bookkeeping_core.models import Client
from bookkeeping.client.forms import ClientForm


__author__ = 'ceasaro'


class ClientView(TemplateView):

    def get_context_data(self, **kwargs):
        context = super(ClientView, self).get_context_data(**kwargs)
        context.update({'clients': Client.objects.all()})
        return context


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
