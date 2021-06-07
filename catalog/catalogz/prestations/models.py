from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length= 200)
    email = models.EmailField()
    sujet = models.TextField()
    message = models.TextField()
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)


    def __str__(self):
        return self.nom

    