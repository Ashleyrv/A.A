from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base' ),
    path('produtos/', views.produtos, name='produtos' ),
    path('usuario/', views.usuario, name='usuario')
   
   
]
