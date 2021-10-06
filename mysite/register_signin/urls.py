from django.urls import path

from .views import *

urlpatterns = [
    path('', authentication, name='authentication'),
    path('logout/', user_logout, name='logout')
]
