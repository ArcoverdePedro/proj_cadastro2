from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('validarcpf/', views.validarcpf, name='validarcpf'),
    path('buscarcep/', views.buscarcep, name='buscarcep'),
    path('validaremail/', views.validaremail, name='validaremail'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    
    ]
