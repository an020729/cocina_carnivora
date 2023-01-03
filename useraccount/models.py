from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.
class Profile(models.Model):
  
    USER_ROLES = (
        (1,'admin'),
        (2,'usuario'),
    )
  
    street        = models.CharField(max_length=150, null=True, blank=True)
    zip           = models.DecimalField(max_digits=5,decimal_places=0, default=0)
    city          = models.CharField(max_length=100, null=True, blank=True)
    country       = models.CharField(max_length=100, null=True, blank=True)
    photo         = models.ImageField('User profile',upload_to="users/",
                                      null=True, blank=True)
    stars_average = models.IntegerField(default=0)
    rate_average = models.IntegerField(default=0)
    user_role     = models.IntegerField(choices=USER_ROLES, default=2)
    user          = models.OneToOneField(User, on_delete=models.CASCADE)


    def __str__(self):
        return f'Perfil de {self.user}'
  
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

post_save.connect(create_profile,sender=User)