from django.db import models

# Create your models here.
class Link(models.Model):

    def __str__(self):
        return self.name
    
    name = models.CharField(max_length=100,null=True,blank=True)
    address = models.CharField(max_length=1000,null=True,blank=True)
