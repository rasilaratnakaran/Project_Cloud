from django.db import models
from django.contrib.auth.models import User
 
# Create your models here.
class user(models.Model):
	FirstName = models.CharField(max_length=255)
	LastName = models.CharField(max_length=255)
	DOB = models.DateField()
	Phone = models.IntegerField()
	email = models.EmailField()
	Address = models.CharField(max_length=255)
	City = models.CharField(max_length=255)
	Country = models.CharField(max_length=255)
	ZipCode = models.CharField(max_length=255)
	Password = models.CharField(max_length=255)
	Image = models.CharField(max_length=255)
	
 
def __str__(self):
    	return self.FirstName
class enquiry(models.Model):
	FirstName = models.CharField(max_length=255)
	LastName = models.CharField(max_length=255)
	Email = models.EmailField()
	PhoneNumber = models.IntegerField()
	Message = models.CharField(max_length=255)

	def __str__(self):
         return self.FirstName
	

class Product(models.Model):
	Category = models.CharField(max_length=255)
	
class SmartPhones(models.Model):
	ProductName = models.CharField(max_length=255)
	BrandName = models.CharField(max_length=255)
	ReleasedDate = models.DateField()
	AverageCost = models.CharField(max_length=255)
	Description = models.CharField(max_length=255)
	Image = models.CharField(max_length=2000)

	def __str__(self):
            return self.ProductName

class SmartWatches(models.Model):
	ProductName = models.CharField(max_length=255)
	BrandName = models.CharField(max_length=255)
	ReleasedDate = models.DateField()
	AverageCost = models.CharField(max_length=255)
	Description = models.CharField(max_length=255)
	Image = models.CharField(max_length=2000)

def __str__(self):
            return self.ProductName

class Televisions(models.Model):
	ProductName = models.CharField(max_length=255)
	BrandName = models.CharField(max_length=255)
	ReleasedDate = models.DateField()
	AverageCost = models.CharField(max_length=255)
	Description = models.CharField(max_length=255)
	Image = models.CharField(max_length=2000)

def __str__(self):
         return self.ProductName

	
