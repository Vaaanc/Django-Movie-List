from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    url(r'^$',
        views.MovieListView.as_view(), name='movie_list'),
    url(r'^(?P<slug>[-\w]+)/$',
        views.MovieDetailView.as_view(), name='movie_detail'),
    url(r'^add_movie',
        login_required(views.MovieCreateView.as_view()), name='add_movie'),
    url(r'^(?P<slug>[-\w]+)/edit/$',
        login_required(views.MovieUpdateView.as_view()), name='update_movie'),
    url(r'^(?P<slug>[-\w]+)/delete/$',
        login_required(views.MovieSoftDeleteView.as_view()), name='soft_delete_movie'),
    url(r'^(?P<slug>[-\w]+)/like/$',
        login_required(views.MovieLikeView.as_view()), name='likes_movie'),
]
