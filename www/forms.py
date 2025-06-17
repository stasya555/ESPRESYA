from django import forms

from .models import *

class DrinkForm(forms.ModelForm):
    class Meta:
        model = Drink
        fields = '__all__'


class PosterForm(forms.ModelForm):
    class Meta:
        model = Poster
        fields = '__all__'