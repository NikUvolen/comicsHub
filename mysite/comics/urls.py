from django.urls import path

from .views import *

urlpatterns = [
    path('', HomeViewComics.as_view(), name='home'),
    path('add-comics/', add_comics, name='add_comics'),
    path('view-comics/<slug:comics_slug>/', ViewComicsDetail.as_view(), name='view_comics')
]
