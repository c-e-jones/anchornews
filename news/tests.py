from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from .models import Post, Comment
from .forms import CommentForm

# Create your tests here.

class TestPostViews(TestCase):
    
    # This will set up 2 accounts, and build a test post, allowing checks
    # to be carried out.

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="testusername",
            password="testpassword",
            email="testemail@email.com"
        )

        self.post = Post(
            title="test title", slug='test-title',
            author=self.user, genre="Local Government, Local Government",
            byline="Test byline", body="Test body",
            created_on="2024-08-13", status=1
        )
        self.post.save()

        self.other_user=User.objects.create_user(
            username="testusername2",
            password="testpassword2",
            email="testemail2@email.com"
        )

    def test_article_page_with_comment_form(self):
        response = self.client.get(reverse('article', args=['test-title']))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"test title", response.content)
        self.assertIn(b"Test body", response.content)
        self.assertIsInstance(response.context['comment_form'], CommentForm)


    # Tests for basic login functions

    def test_post_comment(self):
        self.client.login(
            username="testusername", password="testpassword")
        post_data = {
            'body': 'wow'
            }
        response = self.client.post(reverse(
            'article', args=['test-title']), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Comment submitted.',
            response.content
        )



    # Test for whether a comment is posted appropriately


    