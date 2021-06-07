from django.db import models


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



class liensociaux(models.Model):
    nom = models.CharField(max_length = 200)
    icone = models.CharField(max_length=200)
    liens = models.TextField()
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)


    def __str__(self):
        return self.nom


class Temoignages(models.Model):
    photo = models.FileField(upload_to= 'image_Site')
    nom = models.CharField(max_length = 200)
    poste = models.CharField(max_length = 200)
    message = models.TextField()
    liensociaux = models.TextField()
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)


    def __str__(self):
        return self.nom


class Website(models.Model):
    titre_Latestphoto = models.CharField(max_length = 200)
    nom_Site = models.CharField(max_length=200)
    adresse = models.CharField(max_length=200)
    map = models.TextField()
    titre_Contact = models.CharField(max_length=200)
    titre_videolatest= models.CharField(max_length=200)
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.adresse


