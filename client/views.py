from django.shortcuts import render
from django.http import HttpResponse
from .models import Client

# Create your views here.
def list_client(request,id):
    client = Client.objects.get(id=id)
    commande = client.commande_set.all()
    context = {'client': client, 'cmds':commande}
    return render(request,'client/liste.html',context=context)