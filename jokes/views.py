from django.shortcuts import render
from .forms import JokeForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    CreateView, DetailView, ListView, UpdateView, DeleteView
)
from django.urls import reverse_lazy

from .models import Joke

class JokeDetailView(DetailView):
    model = Joke

class JokeListView(ListView):
    model = Joke

class JokeCreateView(LoginRequiredMixin, CreateView):
    model = Joke
    form_class = JokeForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class JokeUpdateView(UpdateView):
    model = Joke
    form_class = JokeForm

    
class JokeDeleteView(UserPassesTestMixin, DeleteView):
    model = Joke
    success_url = reverse_lazy('jokes:list')
    
    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.user


class JokeUpdateView(UserPassesTestMixin, UpdateView):
    model = Joke
    form_class = JokeForm
    
    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.user
