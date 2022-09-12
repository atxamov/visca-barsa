from django.db import models


# Create your models here.

class Publisher(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    email = models.CharField(max_length=30)
    logo = models.ImageField(upload_to='publisher-logo', null=True)

    def __str__(self) -> str:
        return self.name   

class Book(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='book-images', null=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self) -> str:
        return self.name


class Journalist(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    email = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name   
        
class Mananger(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    email = models.CharField(max_length=30)
    logo = models.ImageField(upload_to='publisher-logo', null=True)

    def __str__(self) -> str:
        return self.name   

class NationalT(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.name   