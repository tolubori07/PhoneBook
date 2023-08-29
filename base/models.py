from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Contacts(models.Model):
    first_name = models.CharField(null=False, blank=False, max_length=100)
    last_name = models.CharField(null=True, blank=True, max_length=100)
    phone_number = PhoneNumberField(blank=True)
    email = models.EmailField(unique=False)
    avatar = models.ImageField(null=True, default="default.png")
    address = models.CharField(null=True, blank=True, max_length=256)
    sociallinks = models.CharField(null=True, blank=True, max_length=256)
    user = models.ForeignKey('User', blank=True,null=True, on_delete=models.CASCADE,related_name='contacts_user')
    favourites = models.BooleanField(default=False)
    Emergency = models.BooleanField(default=False)
    def __str__(self):
         return self.first_name

class User(AbstractUser):
    first_name = models.CharField(null=False, blank=False, max_length=100)
    last_name = models.CharField(null=True, blank=True, max_length=100)
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    bio = models.CharField(max_length=200, null=True)
    avatar = models.ImageField(null=True, default="default.png")
    address = models.CharField(null=True, blank=True, max_length=256)
    sociallinks = models.CharField(null=True, blank=True, max_length=256)
    phone_number = PhoneNumberField(blank=True)
    contacts = models.ForeignKey(Contacts, blank=True, null=True, on_delete=models.CASCADE, related_name='user_contacts')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']