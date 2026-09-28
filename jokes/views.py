from django.shortcuts import render
from .forms import JokeForm
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
    form_class = JokeForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class JokeUpdateView(UpdateView):
    model = Joke
    form_class = JokeForm

class JokeDeleteView(DeleteView):
    model = Joke
    success_url = reverse_lazy('jokes:list')



# Create your views here.
