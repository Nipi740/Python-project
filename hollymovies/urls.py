from django.contrib import admin
from django.urls import path
from viewer.views import MovieCreateView, MovieListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MovieListView.as_view(), name='index'),
    path('movie/create/', MovieCreateView.as_view(), name='movie_create'),
    path('movies/', MovieListView.as_view(), name='movies'),
]