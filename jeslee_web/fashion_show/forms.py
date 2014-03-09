from django.forms import ModelForm
from django import forms
from django.utils.translation import ugettext as _
from jeslee_web.fashion_show.models import FashionRegistration, FashionShow

__author__ = 'ceasaro'


class FashionRegistrationForm(ModelForm):
    MIN_AGE = 3
    MAX_AGE = 25

    fashion_show = forms.ModelChoiceField(queryset=FashionShow.objects.get_upcoming_shows(),
                                          empty_label=_(u"Choose a fashion show"), label=_(u"Fashion show"),
                                          error_messages={'required': _(u'We need to know which show you like to participate')})
    name = forms.CharField(error_messages={'required': _(u'We would like to have your name')})
    age = forms.IntegerField(error_messages={'required': _(u'We need your age to know which model can fit'),
                                             'invalid': _(u'We are looking for persons with there age between {} and {}'.format(MIN_AGE, MAX_AGE))})
    email = forms.CharField(error_messages={'required': _(u'We need your email to get back to you :-)')})


    class Meta:
        model = FashionRegistration
        fields = ['name', 'age', 'email', 'city', 'fashion_show']

    def clean_age(self):
        age = self.cleaned_data['age']

        if age < self.min_age or age > self.max_age:
            self.fields['age'].error_messages['age_between'] \
                = 'We are looking for persons with there age between {} and {}'.format(self.min_age, self.max_age)
            raise forms.ValidationError(self.fields['age'].error_messages["age_between"])
        return age