from django.urls import path
from .views import CompanyView

urlpatterns =[
    path('companies/', CompanyView.as_view(), name='companie_list'),
    path('company/<int:id>', CompanyView.as_view(), name='companise_process'),

]