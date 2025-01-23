from django.urls import path
from .views import *

app_name = 'pages'


urlpatterns = [

    path('home/',home_pages_view,name='home'),
    
    path('',home_pages_view,name='home')
]