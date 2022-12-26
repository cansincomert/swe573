from django.test import TestCase
from django.urls import reverse

from . import models

class PostListViewTests(TestCase):
    def setUp(self):
        # Create some test posts
        user = User.objects.create_user(username='testuser', password='12345')
        group = Group.objects.create(name='testgroup')
        for i in range(1, 4):
            models.Post.objects.create(
                message='Test post %d' % i,
                user=user,
                group=group
            )

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/posts/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('posts:all'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('posts:all'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'posts/post_list.html')

    def test_pagination_is_five(self):
        resp = self.client.get(reverse('posts:all'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue(len(resp.context['post_list']) == 5)

    def test_lists_all_posts(self):
        # Get second page and confirm it has (exactly) remaining 1 items
        resp = self.client.get(reverse('posts:all')+'?page=2')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue(len(resp.context['post_list']) == 1)
