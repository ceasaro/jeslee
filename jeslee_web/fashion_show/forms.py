from django.forms import ModelForm
from django import forms
from django.utils.translation import ugettext_lazy as _
from jeslee_web.fashion_show.models import FashionRegistration, FashionShow

__author__ = 'ceasaro'


class FashionRegistrationForm(ModelForm):
    MIN_AGE = 3
    MAX_AGE = 125

    fashion_show = forms.ModelChoiceField(queryset=FashionShow.objects.get_upcoming_shows(),
                                          empty_label=_(u"Choose a fashion show to participate"),
                                          label=_(u"Fashion show"),
                                          error_messages={'required': _(u'We need to know which show you like to participate')})
    name = forms.CharField(label=_(u'Name'),
                           error_messages={'required': _(u'We would like to have your name')})
    age = forms.IntegerField(label=_(u'Age'),
                             error_messages={'required': _(u'We need your age to know which model can fit'),
                                             'invalid': _(u"We don't recognize your age?".format(MIN_AGE, MAX_AGE))})
    email = forms.CharField(label=_(u'Email'),
                            error_messages={'required': _(u'We need your email to get back to you :-)')})

    class Meta:
        model = FashionRegistration
        widgets = {
            'remarks': forms.Textarea(attrs={'rows': 4, 'cols': 15}),
        }
        fields = ['name', 'age', 'email', 'fashion_show', 'remarks']

    # def clean_age(self):
    #     age = self.cleaned_data['age']
    #
    #     if age < self.MIN_AGE or age > self.MAX_AGE:
    #         self.fields['age'].error_messages['age_between'] \
    #             = _(u'We are looking for persons with there age between {} and {}'.format(self.MIN_AGE, self.MAX_AGE))
    #         raise forms.ValidationError(self.fields['age'].error_messages["age_between"])
    #     return age