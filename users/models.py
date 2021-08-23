from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
'''Model for Users'''


'''Model for Address'''
class Address(models.Model):
    street = models.CharField()
    city = models.CharField()
    province = models.CharField()
    apartment_number = models.CharField()
    postal_code = models.CharField()
    

'''Model Contact'''
class Contact(models.Model):
    phone_number = models.CharField(max_length=10) 
    url = models.URLField()
    # social_media = models.
    # contact email if email different from User.email




class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=50)
   




'''Model for User Profile'''
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    address = models.ForeignKey(Address)
    


