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
    number = models.IntegerField(null=True, blank=True)
    url = models.CharField(max_length=200, null=True, blank=True)
    photo = models.ImageField(upload_to='media/', null=True, blank=True)
    place = models.ForeignKey('Place', on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return self.url
