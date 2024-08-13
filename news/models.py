from django.db import models
from django.contrib.auth.models import User

# Create your models here.

PUBLISH_CONTROL = ((0, "Unpublished"), (1, "Published"))

class Post(models.Model):
        # This is the data model for posts
    title = models.CharField(
        max_length=150, unique=True,
        help_text='What is the title of this article?'
    )
    slug = models.SlugField(
        max_length=200, unique=True,
        help_text="What is the slug for this article?"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True,
        help_text="Which user created this article?"
    )
    genre = models.CharField(
        max_length=50, choices=[
            ("Local Government", "Local Government"),
            ("National News", "National News"),
            ("Tech", "Tech"),
            ("Local Events", "Local Events"),
            ("Reguional Affairs", "Regional Affairs"),
            ("Business", "Business"),
            ("Food", "Food"),
            ("Tourism", "Tourism"),
            ("Sports", "Sports"),
            ("Arts and Culture", "Arts and Culture"),
            ("Finance", "Finance"),
            ("Crime", "Crime")
        ], help_text="What genre of news is this article?", default="0")
    byline = models.CharField(max_length=150, help_text="What is your byline?")
    body = models.TextField()
    created_on = models.DateTimeField(help_text="When will this be posted?")
    updated_on = models.DateTimeField(auto_now=True, help_text="When was this updated?")
    objects = models.Manager()
    status = models.IntegerField(choices=PUBLISH_CONTROL, default=0)