from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Theme(models.Model):
    Newchat = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.Newchat)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.Newchat
    
class Message(models.Model):
    Theme = models.ForeignKey(Theme, related_name="message", on_delete=models.CASCADE, default=1)
    role=models.CharField(max_length=255,default='system')
    message = models.TextField()
    data_added = models.DateTimeField(auto_now_add=True)
    #res_content = models.TextField(null=True, blank=True)

