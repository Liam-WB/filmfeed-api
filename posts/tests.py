from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework import APITestCase


class PostListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='john', password='password')

    def test_can_list_posts(self):
        john = User.objects.get(username='john')
        Post.objects.create(owner=john, title='a title')
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))