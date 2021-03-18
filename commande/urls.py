from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.list_commande),
    path('ajout/',views.ajout_commande,name='ajout_cmd'),
    path('modif/<int:id>',views.modif_commande,name='modif_cmd'),
    path('supprimer/<int:id>',views.delete_commande,name='delete_cmd'),
]