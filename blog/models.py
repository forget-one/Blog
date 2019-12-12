from django.db import models
from .models import *
from django.utils.text import slugify
from time import time 
# Create your models here.

def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))

class Post(models.Model):
    title = models.CharField(max_length=128, db_index=True)
    slug = models.SlugField(unique=True, blank=True)
    body = models.TextField(db_index=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
    date_pub = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.title)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)
    
    class Meta:
        ordering = ['-date_pub']


class Tag(models.Model):
    title = models.CharField(max_length=36)
    slug = models.SlugField(unique=True, blank=True)
    
    def __str__(self):
        return '{}'.format(self.title)

    def save(self, *args, **kwargs):
        if self.slug.replace(' ', '') == '':
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)
        
    class Meta:
        ordering = ['title']