from django.db import models
from tinymce import models as tinymce_models


class Place(models.Model):
    title = models.CharField(max_length=200)
    description_short = models.TextField(blank=True)
    description_long = tinymce_models.HTMLField(blank=True)
    lng = models.FloatField()
    lat = models.FloatField()

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Image(models.Model):
    order = models.PositiveSmallIntegerField(default=0, verbose_name='Позиция')
    photo = models.ImageField()
    place = models.ForeignKey('Place', on_delete=models.CASCADE, related_name='images')

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.place.title





