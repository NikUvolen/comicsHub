from django.urls import path

from .views import *

urlpatterns = [
    path('', HomeViewComics.as_view(), name='home'),
    path('add-comics/', add_comics, name='add_comics'),
    path('view-comics/<int:comics_id>', ViewComicsDetail.as_view(), name='view_comics')
]
