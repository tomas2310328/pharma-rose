from django.contrib import admin
from .models import Checking
from django.contrib.auth.models import User, Group
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.



class CheckingResource(resources.ModelResource):
    class Meta:
        model = Checking
        fields = ('product', 'bar_code', 'serial_number',)


class CheckingAdmin(ImportExportModelAdmin):
    resource_class = CheckingResource
    list_display = ('product', 'serial_number', 'bar_code',)
    list_filter = ('product',)
    search_fields = ('product',)



admin.site.register(Checking, CheckingAdmin)

admin.site.unregister(User)
admin.site.unregister(Group)
