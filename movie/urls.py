from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.MovieListView.as_view(), name = 'movie_list'),
    url(r'^(?P<slug>[-\w]+)/$', views.MovieDetailView.as_view(), name = 'movie_detail'),
    url(r'^add_movie', views.AddMovieView.as_view(), name = 'add_movie'),
    url(r'^(?P<slug>[-\w]+)/edit/$', views.UpdateMovieView.as_view(), name = 'update_movie'),

]
