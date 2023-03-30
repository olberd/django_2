from django.contrib import admin
from places.models import Place, Image


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    fields = ('title', 'description_shot', 'description_long', 'lat', 'lng')


@admin.register(Image)
class ImagesAdmin(admin.ModelAdmin):
    fields = ('order', 'place', 'url', 'photo')
    list_display = ('place', 'order', 'url', 'photo')
