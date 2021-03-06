from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.core.urlresolvers import reverse


# Create your models here.
class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="images_created")
    title = models.CharField(max_length=200, blank=True, null=True)
    url = models.URLField()
    slug = models.SlugField(max_length=200, blank=True)
    image = models.ImageField(upload_to="images/%Y/%m/%d/", blank=True, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    user_liked = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="images_liked", blank=True)


    def __str__(self):
        return self.title
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        
        super(Image, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("images:image_detail", args=[self.id, self.slug])