from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=120)
    text = models.TextField(default='')
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title