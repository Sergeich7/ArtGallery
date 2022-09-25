from django.test import TestCase
from django.urls import reverse


class Password_change_doneViewTest(TestCase):

    def test_text_content(self):

        resp = self.client.get('/users/password-change-done/')
        self.assertEqual(resp.status_code, 200)

        resp = self.client.get(reverse('users:password-change-done'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'users/password-change-done.html')


