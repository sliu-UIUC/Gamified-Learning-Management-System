from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# when a user is received, send the signal 'post_save'
@receiver(post_save, sender=User)
def create_profiel(sender, instance, created, **kwargs):
  if created: #receiver received this function to create a file
    Profile.objects.create(user=instance)
# kwargs receive any additional key word arguments at the end of the function


@receiver(post_save, sender=User)
def save_profiel(sender, instance, **kwargs):
  instance.profile.save()