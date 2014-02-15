from django.forms import ModelForm
from jeslee_web.fashion_show.models import FashionRegistration

__author__ = 'ceasaro'


class FashionRegistrationForm(ModelForm):
    class Meta:
        model=FashionRegistration
        fields = ['name', 'birth_date', 'email', 'street' , 'street_nr', 'zip', 'city']