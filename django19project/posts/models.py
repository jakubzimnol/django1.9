from django.db import models
from django.core.urlresolvers import reverse

def upload_location(instance, filename):
    return "%s/%s" %(instance.id, filename)

class Post(models.Model):
    title = models.CharField(max_length=120)
    text = models.TextField(default='')
    image = models.ImageField(upload_to=upload_location, 
                              null=True,
                              blank=True,
                              height_field='height_image', 
                              width_field='width_image')
    height_image = models.IntegerField(default=0)
    width_image = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"id": self.id})

    class Meta:
        ordering = ['-created','-updated','id']