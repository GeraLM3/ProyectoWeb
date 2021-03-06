from email.policy import default
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from pickle import TRUE
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(User, upload_to = "autenticacion", null = True, blank = True)
    bibliografia = models.TextField(User, null = True, blank = True)
    

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()