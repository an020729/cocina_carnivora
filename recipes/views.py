from django.shortcuts import render, redirect, get_object_or_404
from recipes.forms import RecipeForm
from django.contrib.auth.models import User
from . models import Recipe
from django.contrib import messages
# Create your views here.


#creando una receta 
def create_recipe(request):
   if request.user.is_authenticated:
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            formulario = form.save(commit=False)
            user = User.objects.get(username = request.user.username)
            formulario.user_id = user
            form.save()
            messages.success(request,'Felicidades!, acabas de publicar')  
            return redirect('home')
                 
                    
        context = { 
            'form': form,
        }
   
        return render(request, 'recipe.html', context)
   else:
        return render(request, 'recipe.html')

def get_all_recipes(request):
    if request.method == "GET":
      recipes = Recipe.objects.all()
      return render(request, 'recipe_publications.html', {'recipes':recipes})


def recipe_details(request, id):
    if request.user.is_authenticated:
        details = get_object_or_404(Recipe, id = id) 
        return render(request, 'recipe_details.html', {'details':details})
    else:
         return render(request, 'homepage/index.html')
