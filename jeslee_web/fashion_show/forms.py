from django.forms import ModelForm
from django import forms
from jeslee_web.fashion_show.models import FashionRegistration

__author__ = 'ceasaro'


class FashionRegistrationForm(ModelForm):
    FASHION_SHOW_OPTIONS = (
        ("1", "Drachten, Fries Congrescentrum"),
        ("2", "Winschoten, de Sporthal"),
        ("3", "Zwolle, Multifunctioneel Centrum SIO"),
    )
    fashion_show = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                          choices=FASHION_SHOW_OPTIONS)

    class Meta:
        model = FashionRegistration
        fields = ['name', 'age', 'email', 'city', 'fashion_show']