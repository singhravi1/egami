from django.db import models

# Create your models here.

class Image_client(models.Model):
    """
    Ce modele contient un seul element principal: Image.
    Les deux autres sont automatiquement remplis par Pillow
    """
    image = models.ImageField(null=False, blank=False, height_field='height_field', width_field='width_field')
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)

    def __str__(self):
        return self.image
