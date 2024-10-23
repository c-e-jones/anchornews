from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from .models import Post, Comment

# Create your tests here.

class TestPostViews(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_superuser(
            username = "testusername",
            password = "testpassword",
            email = "testemail@email.com"
        )
        self.post = Post(
            title="Test title", slug="test-title",
            author=self.user, genre="Local Government, Local Government",
            byline="Test byline", body="Test body")
        self.post.save()

