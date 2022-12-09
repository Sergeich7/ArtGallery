from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse


class LoginTest(TestCase):

    def test_login_abs_tmp(self):
        resp = self.client.get('/users/login/', follow=True)
        self.assertEqual(resp.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(resp, 'users/login.html')

    def test_login_rev(self):
        resp = self.client.get(reverse('users:login'), follow=True)
        self.assertEqual(resp.status_code, HTTPStatus.OK)

