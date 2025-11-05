from django.urls import path

from mainApp import admin
from .views import *

urlpatterns = [
    path('', HomeViews.as_view(), name='home'),
    path('/about', AboutViews.as_view(), name='about')
]