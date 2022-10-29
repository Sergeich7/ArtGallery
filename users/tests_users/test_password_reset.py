from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse


class Password_resetViewTest(TestCase):

    def test_password_reset_abs_tmp(self):
        resp = self.client.get('/users/password-reset/', follow=True)
        self.assertEqual(resp.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(resp, 'users/password-reset.html')

    def test_password_reset_rev(self):
        resp = self.client.get(reverse('users:password-reset'), follow=True)
        self.assertEqual(resp.status_code, HTTPStatus.OK)


