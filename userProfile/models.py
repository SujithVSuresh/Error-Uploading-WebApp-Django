from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class UserProfile(models.Model):
    user_name = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    name = models.CharField(max_length=35, blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True)
    birthday = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=55, null=True, blank=True)
    followers = models.ManyToManyField(User, related_name='followers', blank=True)

    def __str__(self):
        return str(self.user_name)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user_name=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


