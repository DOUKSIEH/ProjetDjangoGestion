from django.shortcuts import render
from django.http import HttpResponse
# from .models import Produit

# Create your views here.
def list_commande(request):
    return render(request,'commande/liste.html')

def ajout_commande(request):
    return render(request,'commande/ajout.html')