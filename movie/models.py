# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify


class IsActiveManager(models.Manager):
    def get_queryset(self):
        return super(IsActiveManager, self).get_queryset()\
            .filter(is_active=True)


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200)
    body = models.TextField()
    picture = models.ImageField(upload_to='movie_images', blank=True)
    is_active = models.BooleanField(default=True)
    likes = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = models.Manager()  # Default Manager
    active = IsActiveManager()  # Custom Manager - Get all active movie

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.id is None:
            self.slug = slugify(self.title)
        self.slug = slugify(self.title)
        super(Movie, self).save(*args, **kwargs)
