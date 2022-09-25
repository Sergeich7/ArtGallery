from django.test import TestCase
from django.urls import reverse


class Password_reset_completeViewTest(TestCase):

    def test_text_content(self):

        resp = self.client.get('/users/reset/done/')
        self.assertEqual(resp.status_code, 200)

        resp = self.client.get(reverse('users:password-reset-complete'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'users/password-reset-complete.html')


