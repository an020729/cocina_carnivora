# Generated by Django 4.1.5 on 2023-01-02 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_role',
            field=models.IntegerField(choices=[(1, 'admin'), (2, 'usuario')], default=2),
        ),
    ]
