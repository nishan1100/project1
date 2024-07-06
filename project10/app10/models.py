from django.db import models

# Create your models here.
class login(models.Model):
    Name=models.CharField(max_length=10)
    Age=models.IntegerField()
    Place=models.CharField(max_length=10)
    Photo=models.ImageField(upload_to='media/',null=True,blank=True)
    Email=models.EmailField()
    Password=models.CharField(max_length=10)

class Gallery(models.Model): 
   Brand=models.CharField(max_length=10)
   Name=models.CharField(max_length=10)
   Photo=models.ImageField(upload_to='media/',null=True,blank=True)
   Price=models.IntegerField()


