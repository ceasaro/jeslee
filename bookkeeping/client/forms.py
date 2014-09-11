from django import forms
from django.contrib.auth.models import User

from bookkeeping.bookkeeping_core.models import Client


__author__ = 'ceasaro'


class ClientForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Client
        fields = ['name', 'email', 'street', 'street_nr', 'zip', 'city', 'country']

    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.user_id:
            self.fields['email'].initial = self.instance.user.email

    def save(self, commit=True):
        email = self.cleaned_data['email']
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            password = User.objects.make_random_password()
            user = User.objects.create_user(email, email, password)
        client = super(ClientForm, self).save(False)
        client.user = user
        client.save()
        return client

