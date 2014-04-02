# Create your views here.
from django.core.urlresolvers import reverse
from django.views.generic import  CreateView, UpdateView, DetailView
from django.views.generic.base import ContextMixin
from jeslee_web.fashion_show.forms import FashionRegistrationForm
from jeslee_web.fashion_show.models import FashionRegistration, FashionShow
from jeslee_web.utils.email import send_email


class UpcomingFashionShowMixin(ContextMixin):

    def get_upcoming_fashion_show(self):
        return FashionShow.objects.get_upcoming_show()

    def get_context_data(self, **kwargs):
        context = super(UpcomingFashionShowMixin, self).get_context_data(**kwargs)
        context['upcoming_fashion_show'] = self.get_upcoming_fashion_show()
        return context


class FashionShowsMixin(ContextMixin):

    def get_context_data(self, **kwargs):
        context_data = super(FashionShowsMixin, self).get_context_data(**kwargs)
        context_data['fashion_shows'] = FashionShow.objects.get_upcoming_shows()
        return context_data


class FashionRegistrationCreateView(CreateView):
    form_class = FashionRegistrationForm
    model = FashionRegistration

    def get_success_url(self):

        email_context = dict()
        email_context['registration'] = self.object
        send_email(email_template_name='email/fashion_show/registration-confirmation',
                   recipient_list=[self.object.email],
                   context_dict=email_context)
        return reverse('fashion-registration-thanks', args=(self.object.id, ))


class FashionRegistrationDetailView(DetailView):
    model = FashionRegistration
    context_object_name = 'registration'


class FashionRegistrationUpdateView(UpdateView):
    model = FashionRegistration


class FashionShowsView(FashionRegistrationCreateView, FashionShowsMixin, UpcomingFashionShowMixin):
    pass


class FashionShowDetailView(DetailView, FashionShowsMixin):
    model = FashionShow
    context_object_name = 'fashion_show'