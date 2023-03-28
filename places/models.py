from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=200)
    description_shot = models.CharField(max_length=250)
    description_long = models.TextField()
    lng = models.FloatField()
    lat = models.FloatField()

    def __str__(self):
        return self.title


class Image(models.Model):
    url = models.CharField(max_length=200, null=True, blank=True)
    place = models.ForeignKey('Place', on_delete=models.CASCADE)

    def __str__(self):
        return self.url
