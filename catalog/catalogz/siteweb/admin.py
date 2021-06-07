from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe


# Register your models here.
@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('views_image', 'nom', 'date_add', 'date_update', 'status')
    list_editable = ('status',)

    def views_image(self, obj):
        return mark_safe(f"<img src='{obj.image.url}' style='height:100px; width:150px' ")
    views_image.short_description = 'apercu des images'
    
    
@admin.register(models.About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('views_image', 'descriptions', 'date_add', 'date_update', 'status')
    list_editable = ('status',)


    def views_image(self, obj):
        return mark_safe(f"<img src='{obj.image.url}' style='height:100px; width:150px' ")
    views_image.short_description = 'apercu des images'


    
@admin.register(models.liensociaux)
class liensociauxAdmin(admin.ModelAdmin):
    list_display = ('nom', 'icone', 'liens', 'date_add', 'date_update', 'status')
    list_editable = ('status',)



@admin.register(models.Temoignages)
class TemoignagesAdmin(admin.ModelAdmin):
    list_display = ('views_image', 'nom', 'poste', 'message', 'liensociaux', 'date_add', 'date_update', 'status')
    list_editable = ('status',)

    def views_image(self, obj):
        return mark_safe(f"<img src='{obj.photo.url}' style='height:100px; width:150px' ")
    views_image.short_description = 'apercu des photos'



@admin.register(models.Website)
class WebsiteAdmin(admin.ModelAdmin):
    list_display = ('titre_Latestphoto', 'nom_Site', 'adresse', 'map', 'titre_Contact', 'titre_videolatest', 'date_add', 'date_update', 'status')
    list_editable = ('status',)