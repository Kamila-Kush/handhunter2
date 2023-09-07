from django.urls import path
from .views import *

urlpatterns = [
    path('', company_list, name='company-list'),
    path('<int:id>/', company_detail, name='company-detail')

]