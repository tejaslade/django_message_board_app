from django.test import TestCase
from .models import Post
from django.urls import reverse

class PostModelTest(TestCase):

    def setUp(self):
        Post.objects.create(text = 'just a test')

    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_text = f"{post.text}"
        self.assertEqual(expected_text,'just a test')


class HomePageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(text='this is another test')

    def test_view_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_200_home_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_case_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')