from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.views import generic
from .models import Post, Comment
from django.contrib.auth.decorators import login_required

# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "news/index.html"
    paginate_by = 5

def article(request, slug):
    """ 
    display an article
    
    context:
    
    ``article``
        an instance of :model:`blog.Post`

    template:

    :template:`blog/article.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "news/article.html", {"post": post},
    )
