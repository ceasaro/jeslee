# Create your views here.
from django.views.generic.base import TemplateView
from jeslee_web.fashion_show.views import UpcomingFashionShowMixin


class HomeView(UpcomingFashionShowMixin, TemplateView):
    pass
