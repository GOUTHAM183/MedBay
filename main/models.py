from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(null=True,blank=True,upload_to='MedBay/media')
    content = RichTextField(blank=True,null=True)
    
    date_posted = models.DateTimeField(default=timezone.now)
   
    
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})


class Scheme(models.Model):
    title = title = models.CharField(max_length=100)
    image = models.ImageField(null=True,blank=True,upload_to='MedBay/media')
    content = RichTextField(blank=True,null=True)
    
    date_posted = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("scheme-detail", kwargs={"pk": self.pk})