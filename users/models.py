from django.db import models


class Home(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    price = models.CharField(max_length=10)
    Category=models.ForeignKey("Category", on_delete=models.CASCADE)
    Country=models.CharField( max_length=50)
    image=models.ImageField(upload_to='media_files/')
    
    
    def __str__(self):
        return self.title
class Category(models.Model):
    name=models.CharField(max_length=25)
    def __str__(self):
        return self.name
    
    
    

# Create your models here.
