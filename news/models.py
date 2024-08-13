from django.db import models
from django.contrib.auth.models import User

# Create your models here.

PUBLISH_CONTROL = ((0, "Unpublished"), (1, "Published"))

class Post(models.Model):
        # This is the data model for posts
    title = models.CharField(
        max_length=150, unique_for_date='created-on'
    )
    slug = models.SlugField(
        max_length=200, unique_for_date='created-on'
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True
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
        ])
    byline = models.CharField(max_length=150)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    status = models.IntegerField(choices=PUBLISH_CONTROL, default=0)