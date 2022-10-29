from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse


class Password_reset_completeViewTest(TestCase):

    def test_password_reset_complete_abs_tmp(self):
        resp = self.client.get('/users/reset/done/', follow=True)
        self.assertEqual(resp.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(resp, 'users/password-reset-complete.html')

    def test_password_reset_complete_rev(self):
        resp = self.client.get(reverse('users:password-reset-complete'), follow=True)
        self.assertEqual(resp.status_code, HTTPStatus.OK)

