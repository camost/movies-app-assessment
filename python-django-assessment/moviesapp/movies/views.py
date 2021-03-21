# -*- coding: utf-8 -*-

"""Movies views."""

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.shortcuts import redirect
from django.http import Http404
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from .models import Movie


class MovieListView(ListView):
    """Show all movies."""
    model = Movie

class MovieDetailView(DetailView):
    """Show the requested movie."""
    model = Movie


class SearchView(ListView):
    model = Movie
    template_name = 'movies/movie_list.html'
    context_object_name = 'all_results'

    def get_queryset(self):
        result = super(SearchView, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
            result = Movie.objects.filter(title__contains=query)
        else:
            result = Movie.objects.all()
        return result

class MovieCreateView(SuccessMessageMixin,CreateView):
    """Create a new movie."""
    model = Movie
    fields = ['title', 'year', 'rated', 'released_on', 'genre', 'director', 'plot','photo']
    success_message = 'The movie created successfully'


class MovieUpdateView(SuccessMessageMixin,UpdateView):
    """Update the requested movie."""
    model = Movie
    fields = ['title','director','released_on']
    success_message = '%(director)s The movie updated successfully'
    error_message='The update has failed'



class MovieDeleteView(SuccessMessageMixin,DeleteView):
    """Delete the requested movie."""
    success_url = reverse_lazy('movies:index')
    success_message = 'The movie deleted successfully'
    model = Movie