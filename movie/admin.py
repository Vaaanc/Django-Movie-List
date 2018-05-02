# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Movie

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_active')
    list_filter = ('title',)
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug' : ('title',)}

# Register your models here.
admin.site.register(Movie, MovieAdmin)
