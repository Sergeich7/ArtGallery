from django.test import TestCase
from django.urls import reverse


class LoginViewTest(TestCase):

    def test_text_content(self):

        resp = self.client.get('/users/login/')
        self.assertEqual(resp.status_code, 200)

        resp = self.client.get(reverse('users:login'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'users/login.html')


