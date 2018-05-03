# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponseRedirect
from .models import Movie
from django.views.generic import ListView, DetailView, CreateView, UpdateView, View
from .forms import MoviePageForm, SoftDeleteForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views.generic.detail import SingleObjectMixin
from datetime import datetime

# Create your views here.
class MovieListView(ListView):
    queryset = Movie.active.all().order_by('title')
    context_object_name = 'movies'
    paginate_by = 10 # 10 Movies per page
    template_name = 'movie/list.html'

    def get_context_data(self, **kwargs):
        context = super(MovieListView, self).get_context_data(**kwargs)

        # GET LAST VISIT
        last_visit = self.request.session.get('latest_visit')
        is_visited = False

        if last_visit:
            # If user already visited, update is_visited to true then visit to print = last visit then update latest to now
            is_visited = True
            self.request.session['visit_to_print'] = last_visit
            self.request.session['latest_visit'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        else:
            # if user didn't visit before, create latest visit to now, then print
            self.request.session['latest_visit'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.request.session['visit_to_print'] = None

        context['visit'] = self.request.session['visit_to_print']
        context['is_visited'] = is_visited

        return context

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

class SoftDeleteView(SuccessMessageMixin, SingleObjectMixin, View):
    model = Movie
    success_message = '%(title)s deleted successfully!'
    success_url = '/movie/'

    def post(self, *args, **kwargs):
        movie = super(SoftDeleteView, self).get_object()
        movie.is_active = False
        messages.success(self.request, movie.title + ' deleted successfully!')
        movie.save()
        return HttpResponseRedirect('/movie/')
