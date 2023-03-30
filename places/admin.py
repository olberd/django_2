from django.contrib import admin
from places.models import Place, Image


class ImagesInline(admin.TabularInline):
    model = Image


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    fields = ('title', 'description_shot', 'description_long', 'lat', 'lng')
    inlines = [
        ImagesInline,
    ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    fields = ('order', 'place', 'photo')
    list_display = ('place', 'order', 'photo')
