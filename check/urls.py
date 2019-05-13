from django.urls import path
from .views import checking_serial
# create urls here


app_name = 'check'





urlpatterns = [
    path('', checking_serial, name='check_serial'),


]
