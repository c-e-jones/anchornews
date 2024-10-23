from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator

# Create your models here.

PUBLISH_CONTROL = ((0, "Unpublished"), (1, "Published"))

REVIEW_CHOICES = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
]


class Post(models.Model):
    # This is the data model for posts
    title = models.CharField(
        validators = [MinLengthValidator(1)],
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
        ], help_text="What genre of news is this article?", default="0"
        )
    byline = models.CharField(
        validators = [MinLengthValidator(1)],
        max_length=150, help_text="What is your byline?"
        )
    body = models.TextField(
        validators = [MinLengthValidator(1)]
    )
    created_on = models.DateTimeField(
        help_text="When was this posted?"
        )
    updated_on = models.DateTimeField(
        auto_now=True, help_text="When was this updated?")
    objects = models.Manager()
    status = models.IntegerField(choices=PUBLISH_CONTROL, default=0)

    class Meta:
        ordering = ['-status']
        get_latest_by = 'status'

    def __str__(self):
        return f'{self.title} | written by {self.author}'


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='commenter')
    comment_title = models.CharField(
        validators = [MinLengthValidator(1)],
        max_length=150, help_text="What is the main theme of your comment?")
    body = models.TextField(
        validators = [MinLengthValidator(1)],
        max_length=600, help_text="What do you want to say in your comment?")
    review = models.CharField(
        validators = [MinLengthValidator(1)],
        max_length=2, choices=REVIEW_CHOICES,
        help_text="How do you rate this article, where 10 is the best?")
    approved = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    edited = models.CharField(max_length=8, choices=(
        ('0', 'Unedited'), (1, 'Edited')), default=0)
    edited_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f'Comment {self.comment_title} by {self.author}'


