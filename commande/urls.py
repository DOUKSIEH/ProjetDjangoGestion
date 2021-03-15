from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.list_commande),
    path('',views.ajout_commande,name='ajout_cmd'),
]