from distutils.log import Log
from nturl2path import url2pathname
from django.urls import path
from .views import *


urlpatterns = [
    path('register', Register, name='register'),
    path('login', Login, name='login'),
]
