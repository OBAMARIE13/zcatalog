from django.db import models
# from tinymce.models import HTMLField

# Create your models here.
class Photo(models.Model):
    image = models.FileField(upload_to ='image_Site')
    nom = models.CharField(max_length=200)
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nom
    
class About(models.Model):
    image = models.FileField(upload_to='image_Site')
    descriptions = models.TextField()
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    
    
    def __str__(self):
        return self.descriptions
    
    