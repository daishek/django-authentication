from django.db import models

# import builtin django User model 
from django.contrib.auth.models import User

# use signals
from django.db.models.signals import post_save 

# import receiver to connect receiver to a signal
from django.dispatch import receiver
#  Create your models here.
''' User model
    username
    password
    first_name
    last_name
    email
'''
class Profile(models.Model):
    # oneToOne relation wityh the User model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name}'

# -----------------------------------------
# how it work? 
# - Signup [create user]
#   - signal
#   - call function -> create_user_profile
#   - create the profile for this user ...
# -----------------------------------------


@receiver(post_save, sender=User) #connect this function with the user [the user sends a signal, reciever took the signal & call the function...]
def create_user_profile(sender, instance, created, **kwargs):
    # check if created
    if created:
        # create the profile...
        Profile.objects.create(
            # instance -> User instance model
            user = instance
        )