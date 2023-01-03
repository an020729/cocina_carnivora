from django.shortcuts import render,redirect
from django.contrib.auth.models import User


# Create your views here.
def home(request):
    
    user_role = "Invitado"
    
    result_set = ""
    if result_set:
        user_role = "Cuidador"
    
    result_set = "*"
    if result_set:
        user_role = "Dueño"   
        
    return render(request, 'homepage/index.html', {'role': user_role })


