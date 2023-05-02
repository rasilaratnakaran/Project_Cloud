
from nis import get_default_domain
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(default = 'default.png', upload_to = 'profile_pics')
    firstname = models.CharField(default = 'SOME STRING',max_length=255)
    lastname = models.CharField(default = 'SOME STRING',max_length=255)
    dob = models.DateField(default=get_default_domain)
    phone =  models.IntegerField(default=0)
    address = models.CharField(default = 'SOME STRING',max_length=255)
    city = models.CharField(default = 'SOME STRING',max_length=255)
    country = models.CharField(default = 'SOME STRING',max_length=255)
    zipCode = models.CharField(default = 'SOME STRING',max_length=255)
    
    def __str__(self):
        return f'Profile for {self.user.username}'
   
                