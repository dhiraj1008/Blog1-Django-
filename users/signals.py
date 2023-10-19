from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
       Profile.objects.create(user=instance)

# this create_profile function runs when a user gets created ..



@receiver(post_save,sender=User)
def post_profile(sender,instance,**kwargs):
     instance.profile.save()

# save_profile function just save our profile everytime user object gets saved .



