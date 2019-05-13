from django.contrib import admin
from .models import Checking
from django.contrib.auth.models import User, Group

# Register your models here.


class CheckingAdmin(admin.ModelAdmin):
    list_display = ['serial_number', 'bar_code']
    search_fields = ['serial_number', 'bar_code']




admin.site.register(Checking, CheckingAdmin)

admin.site.unregister(User)
admin.site.unregister(Group)
