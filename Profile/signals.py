from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import userprofile, flightbookingshistory

def user_profile(sender, instance, created, **kwargs):
  if created:
    userprofile.objects.create(
      user=instance,
      first_name=instance.first_name,
      last_name=instance.last_name,
      email=instance.email,
    )

post_save.connect(user_profile, sender=User)




