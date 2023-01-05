# Generated by Django 4.1.5 on 2023-01-05 21:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='titulo')),
                ('ingredients', models.TextField(verbose_name='descripcion')),
                ('preparation', models.TextField(verbose_name='preparacion')),
                ('picture_recipe', models.ImageField(blank=True, null=True, upload_to='recipes/', verbose_name='foto de la receta')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
