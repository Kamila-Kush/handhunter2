from django.urls import path
from .views import *

urlpatterns = [
    path('', worker_list, name='workers-list'),
    path('<int:id>/', worker_detail, name='worker-detail'),


]