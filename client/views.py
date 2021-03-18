from django.shortcuts import render
from django.http import HttpResponse
from .models import Client
from commande.filters import CommandeFiltre

# Create your views here.
def list_client(request,id):
    client = Client.objects.get(id=id)
    commande = client.commande_set.all()
    myfilters = CommandeFiltre(request.GET,queryset=commande)
    commande = myfilters.qs 
    print(myfilters.qs)
    context = {'client': client, 'cmds':commande,"myfilters":myfilters}
    return render(request,'client/liste.html',context=context)