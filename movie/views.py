# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from .models import Movie
from django.views.generic import ListView, DetailView, CreateView, UpdateView, View
from .forms import MoviePageForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views.generic.detail import SingleObjectMixin
from datetime import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.
class MovieListView(ListView):
    queryset = Movie.active.all().order_by('title')
    context_object_name = 'movies'
    paginate_by = 4 # 4 Movies per page
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
            self.request.session['latest_visit'] = datetime.now().strftime("%b %d %Y %I:%M %p")
        else:
            # if user didn't visit before, create latest visit to now
            self.request.session['latest_visit'] = datetime.now().strftime("%b %d %Y %I:%M %p")
            self.request.session['visit_to_print'] = None

        context['visit'] = self.request.session['visit_to_print']
        context['is_visited'] = is_visited

        return context

class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movie/detail.html'
    context_object_name = 'movie'

    def get_queryset(self):
        queryset = self.model.active.all()

        return queryset

class AddMovieView(SuccessMessageMixin, CreateView):
    form_class = MoviePageForm
    success_url = '/movie/'
    template_name = 'movie/add_movie.html'
    success_message = "%(title)s created successfully!"
    login_required = True

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
    login_required = True

    def get_queryset(self):
        queryset = self.model.active.all()

        return queryset

class SoftDeleteView(SuccessMessageMixin, SingleObjectMixin, View):
    model = Movie
    login_required = True

    def post(self, *args, **kwargs):
        movie = super(SoftDeleteView, self).get_object()
        movie.is_active = False
        messages.success(self.request, movie.title + ' deleted successfully!')
        movie.save()
        return HttpResponseRedirect('/movie/')

class LikeView(SingleObjectMixin, View):
    model = Movie
    login_required = True

    def get(self, *args, **kwargs):
        print self.request.GET['movie_id']
        movie = Movie.objects.get(id = self.request.GET['movie_id'])
        movie.likes += 1
        likes = movie.likes
        movie.save()
        return HttpResponse(likes)
