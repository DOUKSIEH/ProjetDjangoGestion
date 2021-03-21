from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUSer
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
MESSAGE_TAGS = {
    messages.constants.ERROR: 'danger'
}

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
            return redirect('login')
   
    return render(request,'compte/inscription.html',context={'form':form})


def connexion(request):
    # messages.add_message(request, messages.ERROR, 'ERREUR')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(request.POST)
        user = authenticate(request,username=username,password=password)
        
        if user:
            
            login(request,user)
            return redirect("home")
        else:
            messages.error(request,"Veuillez renseignée vos identifiants",'danger')
        
    return render(request,'compte/connexion.html')

def deconnexion(request):
    logout(request)
    return redirect('home')
     
