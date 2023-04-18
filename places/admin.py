from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminBase
from django.contrib import admin
from django.utils.html import format_html

from places.models import Place, Image


class ImagesInline(SortableInlineAdminMixin, admin.TabularInline):
    fields = ('place', ('photo', 'get_img',), 'order',)
    readonly_fields = ('get_img', )
    extra = 1
    model = Image

    def get_img(self, img):
        return format_html('<img src="{}", height=200px />', img.photo.url)


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
