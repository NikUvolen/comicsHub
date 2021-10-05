from django.urls import path

from .views import *

urlpatterns = [
    path('', comics_view_page, name='home')
]
