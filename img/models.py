from django.db import models


class ImageClient(models.Model):
    image = models.FileField(null=False, blank=False)
