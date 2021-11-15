from django.urls import path

from .views import *


urlpatterns = [
    path('', redirect_to_comics, name='redirect_to_comics'),
    path('<slug:username>/', view_user_profile, name='user_profile')
]
