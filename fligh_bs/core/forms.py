from django import forms
from django.forms import fields
from .models import *


class DateInput(forms.DateInput):
    input_type = 'date'

class flightbsForm(forms.ModelForm):
    class Meta:
        model=flightbs

        fields=[
            "passenger_name",
            "Destination",
            "Flight_Name",
            "Date"
        ]
        widgets = {
            'Date': DateInput(),
        }