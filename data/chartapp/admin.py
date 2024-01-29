from django.contrib import admin

from .models import Product

# Register your models here.

admin.site.register(Product)

from .models import EnergyInsight

from import_export import resources
from import_export.admin import ImportExportModelAdmin

class EnergyResource(resources.ModelResource):
    class Meta:
        model = EnergyInsight

class EnergyAdmin(ImportExportModelAdmin) :
    resource_class = EnergyResource

admin.site.register(EnergyInsight,EnergyAdmin)

