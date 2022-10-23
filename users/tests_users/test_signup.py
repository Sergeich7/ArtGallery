from django.test import TestCase
from django.urls import reverse


class SignupViewTest(TestCase):

    def test_signup_abs_tmp(self):
        resp = self.client.get('/users/signup/', follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'users/signup.html')

    def test_signup_rev(self):
        resp = self.client.get(reverse('users:signup'), follow=True)
        self.assertEqual(resp.status_code, 200)


