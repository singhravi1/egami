from django.db import models


class ImageClient(models.Model):
    image = models.ImageField(null=False, blank=False)
