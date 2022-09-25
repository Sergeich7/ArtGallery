from django.test import TestCase
from django.urls import reverse


class Password_reset_doneViewTest(TestCase):

    def test_text_content(self):

        resp = self.client.get('/users/password-reset/done/')
        self.assertEqual(resp.status_code, 200)

        resp = self.client.get(reverse('users:password-reset-done'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'users/password-reset-done.html')


