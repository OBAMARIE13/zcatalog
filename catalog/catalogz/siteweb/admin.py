from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('image', 'nom', 'date_add', 'date_update', 'status')
    
    
@admin.register(models.About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('image', 'descriptions', 'date_add', 'date_update', 'status')