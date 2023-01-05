from django.contrib import admin
from .models import Recipe


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'title', 'ingredients', 'preparation')
    ordering = ('user_id',)
    search_fields = ('user_id', 'title')


admin.site.register(Recipe, RecipeAdmin)