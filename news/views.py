from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import generic
from .models import Post
from .models import Comment

# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "post_list.html"