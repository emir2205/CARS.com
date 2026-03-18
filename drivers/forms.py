from django import forms

from .models import DriverModel


class DriverForm(forms.ModelForm):
    class Meta:
        model = DriverModel
        fields = '__all__'
