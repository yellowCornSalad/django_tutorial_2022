from django.forms import ModelForm
from .models import CountryData

class CountryDataForm(ModelForm):
    class Meta:
        model = CountryData
        fields = '__all__'