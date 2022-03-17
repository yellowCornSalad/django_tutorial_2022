from pydoc import ModuleScanner
from django.contrib import admin

# Register your models here.
from dashboard import models

admin.site.register(models.CountryData)
