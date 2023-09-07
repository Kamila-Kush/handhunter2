from django.urls import path
from .views import *

urlpatterns = [
    path('', worker_list, name='workers-list'),

]