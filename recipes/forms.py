from recipes.models import Recipe
from django import forms

class RecipeForm(forms.ModelForm):



    
    labels = {
        'title': 'Titulo',
        'ingredients': 'Ingredientes',
        'preparation': 'Preparacion',
        'picture_recipe': 'Subir foto',
    }


    widgets = {
        'title': forms.TextInput(
            attrs={
            'class':'form-control',
            'placeholder':'titulo',
            }),

        'ingredients': forms.Textarea(
            attrs={
            'class':'form-control',
            'placeholder':'ingredientes',
            
            }),

        'preparation': forms.Textarea(
            attrs={
            'class':'form-control',
            'placeholder':'preparacion',
            }),

        'picture_recipe': forms.FileInput(
            attrs={
               'required':'True',
               'help_text':'Campo requierido'
            }
        )
    
    }
    
    
    
    class Meta:
        model = Recipe
        fields = ['title', 'ingredients', 'preparation', 'picture_recipe', 'user_id']
        exclude = ['user_id']