from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView


__author__ = 'ceasaro'


class FinancialHomeView(TemplateView):

    @method_decorator(staff_member_required)
    def dispatch(self, *args, **kwargs):
        return super(FinancialHomeView, self).dispatch(*args, **kwargs)
