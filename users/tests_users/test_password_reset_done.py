from django.test import TestCase
from django.urls import reverse


class Password_reset_doneViewTest(TestCase):

    def test_password_reset_done_abs_tmp(self):
        resp = self.client.get('/users/password-reset/done/', follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'users/password-reset-done.html')

    def test_password_reset_done_rev(self):
        resp = self.client.get(reverse('users:password-reset-done'), follow=True)
        self.assertEqual(resp.status_code, 200)


