from django.urls import path
from .views import *

urlpatterns = [
    path('link-add/', create_link, name='linkadd'),
]
