
from django.views.generic import UpdateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from viewer.models import Movie
from viewer.forms import MovieForm
from django.views.generic import ListView


class MovieCreateView(CreateView):
    model = Movie
    form_class = MovieForm
    template_name = 'form.html'
    success_url = reverse_lazy('index')  # Pärast lisamist suunatakse tagasi esilehele.

class MovieUpdateView(UpdateView):
    model = Movie
    form_class = MovieForm
    template_name = 'form.html'
    success_url = reverse_lazy('index')

class MovieListView(ListView):
    model = Movie
    template_name = 'movies.html'
    context_object_name = 'movies'