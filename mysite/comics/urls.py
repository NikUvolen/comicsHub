from django.urls import path

from .views import *

urlpatterns = [
    path('', comics_view_page, name='home'),
    path('add-comics/', add_comics, name='add_comics')
]
