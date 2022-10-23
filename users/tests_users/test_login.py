from django.test import TestCase
from django.urls import reverse


class LoginViewTest(TestCase):

    def test_login_abs_tmp(self):
        resp = self.client.get('/users/login/', follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'users/login.html')

    def test_login_rev(self):
        resp = self.client.get(reverse('users:login'), follow=True)
        self.assertEqual(resp.status_code, 200)


