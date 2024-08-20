from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by("-created_on")
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
    comments = post.comments.all().order_by('-created_on')
    comment_count = post.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()

    comment_form = CommentForm()

    return render(
        request,
        "news/article.html",
        {
            'post': post,
            'comments': comments,
            'comment_count': comment_count,
            "comment_form": comment_form,
        }
    )


""" 
Code for comment edit box
"""

def comment_editor(request, slug, comment_id):
    """
    This is a basic comment editor form view
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment updated successfully.')
        else:
            messages.add_message(request, messages.ERROR, 'Error, could not update comment.')

    return HttpResponseRedirect(reverse('article', args=[slug]))


""" 
Code for comment delete
"""


def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('article', args=[slug]))