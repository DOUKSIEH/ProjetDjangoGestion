from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import CommandeForm
from .models import Commande

# Create your views here.
def list_commande(request):
    return render(request,'commande/liste.html')

def ajout_commande(request):
    
    form = CommandeForm()
    if request.method == 'POST':
        form = CommandeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context= {'forms':form}
    return render(request,'commande/ajout_commande.html',context=context)

def modif_commande(request,id):
    cmd_id = Commande.objects.get(id=id)
    form = CommandeForm(instance=cmd_id)
    if request.method == 'POST':
        form = CommandeForm(request.POST,instance=cmd_id)
        if form.is_valid():
            form.save()
            return redirect('/')
    context= {'forms':form,'id':id}
    return render(request,'commande/ajout_commande.html',context=context)


def delete_commande(request,id):
    cmd_id = Commande.objects.get(id=id)    
    
    if request.method == 'POST':
        cmd_id.delete()
        return redirect('/')
    context= {'del_id':cmd_id}
    return render(request,'commande/delete_commande.html',context=context)