from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import generic
from .models import Post
from .models import Comment

# Create your views here.

class PostList(generic.ListView):
    model = Post