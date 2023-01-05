from django.urls import path
from . import views


urlpatterns =[
    path('register/', views.create_recipe, name='create_recipe'),
    path('all_recipes/', views.get_all_recipes, name='get_recipes'),
    path('recipe_detail/<int:id>', views.recipe_details, name='detail_recipe')
]