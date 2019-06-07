"""pharmarose URL Configuration"""


from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import home, about




urlpatterns = [
    path('eslam-admin/', admin.site.urls),
    path('', home, name='home'),
    path('about-us/', about, name='about'),
    path('products/', include('products.urls', namespace='products')),
    path('check-code/', include('check.urls', namespace='check')),
    path('contact-us/', include('contact.urls', namespace='contact')),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
