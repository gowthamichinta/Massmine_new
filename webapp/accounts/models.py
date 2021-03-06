# accounts/models.py

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from encrypted_model_fields.fields import EncryptedCharField

class SocialPlatformProfile(models.Model):
    profile_id = models.IntegerField()
    consumer_key =  EncryptedCharField(max_length=50, blank=True)
    consumer_secret = EncryptedCharField(max_length=50, blank=True)
    access_token = EncryptedCharField(max_length=50, blank=True)
    access_token_secret = EncryptedCharField(max_length=50, blank=True)
    social_platform = models.TextField(max_length=50)

    def __str__(self):
        return 'SocialPlatformProfile: ' + self.social_platform

class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    consumer_key =  EncryptedCharField(max_length=50, blank=True)
    consumer_secret = EncryptedCharField(max_length=50, blank=True)
    access_token = EncryptedCharField(max_length=50, blank=True)
    access_token_secret = EncryptedCharField(max_length=50, blank=True)
    social_platform = models.TextField(max_length=50)

    def __str__(self):
        return 'Profile: ' + self.user.username

#@receiver(post_save, sender=User)
#def update_user_profile(sender, instance, created, **kwargs):
 #   if created:
  #      Profile.objects.create(user=instance)
   # instance.profile.save()



