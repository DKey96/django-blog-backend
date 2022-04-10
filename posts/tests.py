from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post


class BlogTest(TestCase):
    
    @classmethod
    def setUpTestData(cls) -> None:
        testuser = User.objects.create_user(
            username='testuser1', password='abc123'
        )
        testuser.save()

        test_post = Post.objects.create(
            author=testuser, 
            title='Blog test title',
            body='Test blog body...'
        )
        test_post.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'
        self.assertEqual(author, 'testuser1')
        self.assertEqual(title, 'Blog test title')
        self.assertEqual(body, 'Test blog body...')