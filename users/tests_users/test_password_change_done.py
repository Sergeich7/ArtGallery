from django.test import TestCase
from django.urls import reverse


class Password_change_doneViewTest(TestCase):

    def test_password_change_done_abs_tmp(self):
        resp = self.client.get('/users/password-change-done/', follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'users/password-change-done.html')

    def test_password_change_done_rev(self):
        resp = self.client.get(reverse('users:password-change-done'), follow=True)
        self.assertEqual(resp.status_code, 200)


