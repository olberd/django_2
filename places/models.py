from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=200)
    description_shot = models.CharField(max_length=250)
    description_long = models.TextField()
    lng = models.FloatField()
    lat = models.FloatField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Image(models.Model):
    order = models.PositiveSmallIntegerField(default=0, verbose_name='Позиция', null=True, blank=True)
    photo = models.ImageField(null=True, blank=True)
    place = models.ForeignKey('Place', on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return self.place.title

    class Meta:
        ordering = ['order']



