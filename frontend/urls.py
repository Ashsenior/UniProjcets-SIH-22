from django.urls import path
from .views import *

app_name = "frontend"

urlpatterns = [
    path('',index),
    path('university-form/',index),
]
