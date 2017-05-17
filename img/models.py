from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify


class ImageClient(models.Model):
    
    slug = models.SlugField(unique=True)
    image = models.FileField(null=False, blank=False)

# better urls
def create_slug(instance, new_slug=None):
    slug = slugify('egami')
    if new_slug is not None:
        slug = new_slug
    qs = ImageClient.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, sender=ImageClient)