from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminBase
from django.contrib import admin
from django.utils.html import format_html

from places.models import Place, Image


class ImagesInline(SortableInlineAdminMixin, admin.TabularInline):
    fields = ('place', ('photo', 'place_img',), 'order',)
    readonly_fields = ('place_img', )
    extra = 1
    model = Image

    def place_img(self, img):
        return format_html(f'<img src="{img.photo.url}", height=200px />')


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    fields = ('place', 'photo', 'order',)
    list_display = ('place', 'photo', 'order',)


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    fields = ('title', 'description_short', 'description_long', 'lat', 'lng')
    inlines = [
        ImagesInline,
    ]



