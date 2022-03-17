from django.forms import ModelForm
from .models import CountryData

class CountryDataForm(ModelForm):
    class Meta:
        model = CountryData
        #field = ['country', 'population']
        fields = '__all__'