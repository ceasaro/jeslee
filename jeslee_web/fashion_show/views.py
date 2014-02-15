# Create your views here.
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DetailView
from jeslee_web.fashion_show.forms import FashionRegistrationForm
from jeslee_web.fashion_show.models import FashionRegistration


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
