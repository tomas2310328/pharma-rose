from django.urls import path
from .views import contact
# create urls here


app_name = 'contact'





urlpatterns = [
    path('', contact, name='contact'),


]
