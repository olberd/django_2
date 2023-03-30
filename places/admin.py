from django.contrib import admin
from django.utils.html import format_html

from places.models import Place, Image


class ImagesInline(admin.TabularInline):
    fields = ('place', ('photo', 'place_img',), 'order',)
    readonly_fields = ('place_img', )
    extra = 1
    model = Image

    def place_img(self, img):
        return format_html(f'<img src="{img.photo.url}", height=200px />')


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    fields = ('order', 'place', 'photo')
    list_display = ('place', 'photo', 'order',)


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    fields = ('title', 'description_shot', 'description_long', 'lat', 'lng')
    inlines = [
        ImagesInline,
    ]



