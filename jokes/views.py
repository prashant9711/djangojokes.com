from django.shortcuts import render
from django.views.generic import (
    CreateView, DetailView, ListView, UpdateView, DeleteView
)
from django.urls import reverse_lazy

from .models import Joke

class JokeDetailView(DetailView):
    model = Joke

class JokeListView(ListView):
    model = Joke

class JokeCreateView(CreateView):
    model = Joke
    fields = ['question', 'answer']

class JokeUpdateView(UpdateView):
    model = Joke
    fields = ['question', 'answer']

class JokeDeleteView(DeleteView):
    model = Joke
    success_url = reverse_lazy('jokes:list')



# Create your views here.
