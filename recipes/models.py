from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Recipe(models.Model):

    title = models.CharField('titulo', max_length=255, null=False)
    ingredients = models.TextField('descripcion', null=False)
    preparation = models.TextField('preparacion', null=False)
    picture_recipe = models.ImageField('foto de la receta', upload_to="recipes/", null=True, blank=True)
    #user relationship
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.user_id.username


    class meta: 
        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipes'
        