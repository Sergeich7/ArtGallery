from django.test import TestCase
from django.urls import reverse


class SignupViewTest(TestCase):

    def test_text_content(self):

        resp = self.client.get('/users/signup/')
        self.assertEqual(resp.status_code, 200)

        resp = self.client.get(reverse('users:signup'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'users/signup.html')


