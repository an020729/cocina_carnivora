from recipes.models import Recipe
from django import forms

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'ingredients', 'preparation', 'picture_recipe', 'user_id']
        exclude = ['user_id']
        title = forms.CharField(label='Titulo de la receta', required=False,
             widget=forms.TextInput
             (attrs={
                'class':'form-control',
                'placeholder':'titulo',
             }))   



        ingredients = forms.Textarea(
            attrs={
                'class':'form-control',
            })



        preparation =forms.Textarea(
                attrs={
                'class':'form-control',
                'placeholder':'preparacion',
                })
                
            
        picture_recipe= forms.FileInput(
                attrs={
                'required':'True',
                'help_text':'Campo requierido'
                }
            )




    
   
    
    