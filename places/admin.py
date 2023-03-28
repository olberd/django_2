from django.contrib import admin
from places.models import Place, Image


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    fields = ('title', 'description_shot', 'description_long', 'lng', 'lat')


@admin.register(Image)
class ImagesAdmin(admin.ModelAdmin):
    fields = ('place', 'url')
    list_display = ('place', 'url')
