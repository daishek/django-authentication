from django.db import models

# import builtin django User model 
from django.contrib.auth.models import User
# Create your models here.
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