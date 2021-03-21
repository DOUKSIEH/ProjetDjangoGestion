from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUSer
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.

def inscription(request):
    form = CreateUSer()
    if request.method == 'POST':
        print(request.POST)
        form = CreateUSer(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Votre compte (Mr/Mme {}) a bien été créé !!!'.format(user))
            return redirect('connexion')
   
    return render(request,'compte/inscription.html',context={'form':form})


def connexion(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(request.POST)
        user = authenticate(request,username=username,password=password)
        
        if user:
            
            login(request,user)
            return redirect("home")
        else:
            messages.info(request,"Veuillez renseignée vos identifiants")
        
    return render(request,'compte/connexion.html')

def logout(request):
    logout(request)
    return redirect('home')
     
