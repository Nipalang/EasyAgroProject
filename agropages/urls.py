from django.urls import path 
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('services/', service, name='service'),
    path('products/', product, name='product'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact')
]