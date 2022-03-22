from pydoc import ModuleScanner
from django.contrib import admin
from dashboard import models


class CountryDataAdmin(admin.ModelAdmin):

    list_display = ('country', 'population')


admin.site.register(models.CountryData, CountryDataAdmin)
