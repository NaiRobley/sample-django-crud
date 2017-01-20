from django.db import models
from django.contrib import auth
from django.core.urlresolvers import reverse

# Create your models here.
class Comment(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=1024)
    #image = models.ImageField(upload_to='/uploads/')

    def get_absolute_url(self):
        return reverse('comment_detail', args=[str(self.id)])

    def __str__(self):
        return self.title