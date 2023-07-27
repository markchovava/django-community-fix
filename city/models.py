from django.db import models
from django.conf import settings


class City(models.Model):
   name = models.CharField(max_length=255)
   description = models.TextField(null=True, blank=True) 
   cover_image = models.ImageField(upload_to='images/city', null=True, blank=True)
   user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
   created_at = models.DateField(auto_now_add=True)
   updated_at = models.DateField(auto_now=True)
   
   def __str__(self):
        return self.name