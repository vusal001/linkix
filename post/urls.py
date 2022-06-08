from django.urls import path
from .views import *

urlpatterns = [
    path('link-add/', create_link, name='linkadd'),
    path('<str:slug>', ads_view, name="ads_view")
]
