from django.urls import path
from .views import (
    JokeDetailView, JokeListView, JokeUpdateView, JokeCreateView, JokeDeleteView
)   

app_name = 'jokes'
urlpatterns = [
    path('', JokeListView.as_view(), name='list'),
    path('joke/<slug>/', JokeDetailView.as_view(), name='detail'),
    path('joke/<slug>/update/', JokeUpdateView.as_view(), name='update'),
    path('joke/create/', JokeCreateView.as_view(), name='create'),
    path('joke/<slug>/delete', JokeDeleteView.as_view(), name='delete'),
]