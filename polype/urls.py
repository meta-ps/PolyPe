from django.contrib import admin
from django.urls import path
from polype.views import *

urlpatterns = [

    path('',Home,name='home'),
    path('user/<str:username>/',UserView,name='userview')

]
