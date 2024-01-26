from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

user = get_user_model()


class PersonEventForm(forms.ModelForm):
    class Meta(object):
        model = PersonEvent
        fields = ('title', 'logo', 'description', 'date', 'city', 'address')
        exclude = ('creater', )

        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }
        

class EventForm(forms.ModelForm):
    class Meta(object):
        model = Event
        fields = ('title', 'logo', 'description', 'date', 'city', 'address')
        exclude = ('creater', )

        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }