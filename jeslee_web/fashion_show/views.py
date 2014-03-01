# Create your views here.
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DetailView
from django.views.generic.base import ContextMixin
from jeslee_web.fashion_show.forms import FashionRegistrationForm
from jeslee_web.fashion_show.models import FashionRegistration, FashionShow


class UpcomingFashionShowMixin(ContextMixin):

    def get_upcoming_fashion_show(self):
        return FashionShow.objects.get_upcoming_show()

    def get_context_data(self, **kwargs):
        context = super(UpcomingFashionShowMixin, self).get_context_data(**kwargs)
        context['upcoming_fashion_show'] = self.get_upcoming_fashion_show()
        return context


class FashionRegistrationCreateView(CreateView):
    form_class = FashionRegistrationForm
    model = FashionRegistration

    def get_success_url(self):
        return reverse('fashion-registration-thanks', args=(self.object.id, ))


class FashionRegistrationDetailView(DetailView):
    model = FashionRegistration
    context_object_name = 'registration'


class FashionRegistrationUpdateView(UpdateView):
    model = FashionRegistration
