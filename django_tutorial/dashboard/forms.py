from django.forms import ModelForm
from .models import CountryData, Place


class PlaceForm(ModelForm):
    class Meta:
        model = Place

        fields = '__all__'


class CountryDataForm(ModelForm):
    class Meta:
        model = CountryData
        #field = ['country', 'population']
        fields = '__all__'
