# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Movie
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .forms import MoviePageForm
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
class MovieListView(ListView):
    queryset = Movie.active.all().order_by('title')
    context_object_name = 'movies'
    paginate_by = 5 # 5 Movies per page
    template_name = 'movie/list.html'

class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movie/detail.html'
    context_object_name = 'movie'

class AddMovieView(SuccessMessageMixin, CreateView):
    form_class = MoviePageForm
    success_url = '/movie/'
    template_name = 'movie/add_movie.html'
    success_message = "%(title)s created successfully!"

    def form_valid(self, form):
        new_movie = form.save(commit = False)
        new_movie.save()
        return super(AddMovieView, self).form_valid(form)


class UpdateMovieView(SuccessMessageMixin, UpdateView):
    model = Movie
    form_class = MoviePageForm
    template_name = 'movie/add_movie.html'
    success_message = '%(title)s updated successfully!'
    success_url = '/movie/'
