from wsgiref.util import request_uri
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib import  messages
from django.urls import reverse_lazy
from .forms import RegisterForm, PwdChangingForm, ProfileForm, UsrChangeFrm
from django.views import generic
from useraccount.models import Profile

# Create your views here.

def login_doggy(request):
    if request.user.is_authenticated:
        messages.error(request,'Ya estas logeado ')
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)
        
        if user:
            login(request,user)
            messages.success(request,'Bienvenido de nuevo {}'.format(user.username))
            return redirect('home')

        else:
            messages.error(request,'Usuario o contraseña no validos')
        
    return render(request,'login.html', {})

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = RegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():

        user = form.save()
        if user:
            login(request,user)
            messages.success(request,'Cuenta creada exitosamente')
            return redirect('home')
           

    return render(request,'register.html',{
        'form' : form,
    })

def assign_role(request):
    if request.method == 'POST':
        user_id =request.POST.get('user')
        mod = Profile.objects.create(user = user_id)
        if mod.is_valid():
            mod.save()
            return render(request,'home.html',{})  
  
  
def logout_doggy(request):
    if not request.user.is_authenticated:
        return redirect('home')
    logout(request)
    messages.success(request,'Salió de sesión exitosamente')
    return redirect('home')
  
class UserEditView(generic.UpdateView):
    model = User
    form_class = UsrChangeFrm
    template_name = 'registration/editpro.html'
  
    success_url = reverse_lazy("useraccount:pwdsuccess")
    
    def get_object(self):
      return self.request.user

class UserEditExtendedView(generic.UpdateView):
    model= Profile
    form_class = ProfileForm
    template_name = 'registration/editprofile.html'
    success_url = reverse_lazy("useraccount:pwdsuccess")
    


class PwdChangeView(PasswordChangeView):
    form_class = PwdChangingForm
    success_url = reverse_lazy("useraccount:pwdsuccess")
    
def pwdsuccess(request):
    messages.success(request,'Datos cambiados correctamente')  
    return redirect('home')
    

