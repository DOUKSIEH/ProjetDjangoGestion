from django.urls import path
from . import views

urlpatterns = [
    
    path('connexion',views.connexion,name='login'),
    path('inscription',views.inscription,name='inscription'),
    path('deconnexion',views.deconnexion,name='logout'),
]
