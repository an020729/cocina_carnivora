# Generated by Django 4.1.5 on 2023-01-17 21:04

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='preparation',
            field=ckeditor.fields.RichTextField(),
        ),
    ]