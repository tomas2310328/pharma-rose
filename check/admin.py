from django.contrib import admin
from .models import Checking
from django.contrib.auth.models import User, Group

# Register your models here.


class CheckingAdmin(admin.ModelAdmin):
    list_display = ('product', 'serial_number', 'bar_code',)
    list_filter = ('product',)
    search_fields = ('product',)




admin.site.register(Checking, CheckingAdmin)

admin.site.unregister(User)
admin.site.unregister(Group)
