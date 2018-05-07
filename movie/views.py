# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import HttpResponse
from .models import Movie
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import View
from .forms import MoviePageForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views.generic.detail import SingleObjectMixin
from datetime import datetime
from django.contrib.auth.decorators import login_required


class MovieListView(ListView):
    queryset = Movie.active.all().order_by('title')
    context_object_name = 'movies'
    paginate_by = 4
    template_name = 'movie/list.html'

    def get_context_data(self, **kwargs):
        context = super(MovieListView, self).get_context_data(**kwargs)
        last_visit = self.request.session.get('latest_visit')

        if last_visit:
            # If user already visited,
            # then visit_to_print = latest_visit
            # and update latest_visit to now
            self.request.session['visit_to_print'] = last_visit
            self.request.session['latest_visit'] = datetime.now()\
                .strftime("%b %d %Y %I:%M %p")
        else:
            # If user didn't visit before, create latest visit to now
            self.request.session['latest_visit'] = datetime.now()\
                .strftime("%b %d %Y %I:%M %p")
            self.request.session['visit_to_print'] = None

        context['visit'] = self.request.session['visit_to_print']
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
        new_movie = form.save(commit=False)
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
        movie = Movie.objects.get(id=self.request.GET['movie_id'])
        movie.likes += 1
        likes = movie.likes
        movie.save()
        return HttpResponse(likes)
