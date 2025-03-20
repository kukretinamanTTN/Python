from django.test import TestCase
from .models import Post

class PostTest(TestCase):
    def setUp(self):
        self.post = Post.objects.create(title="post1", content="Hello Post1")
        
    def test_create_post(self):
        self.assertEqual(self.post.title, "post1")
