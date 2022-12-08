from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse


class ThanksViewTest(TestCase):

    def test_thanks_abs_tmp(self):
        resp = self.client.get('/thanks/', follow=True)
        self.assertEqual(resp.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(resp, 'art/email_success.html')

    def test_thanks_abs_rev(self):
        resp = self.client.get(reverse('art:thanks'), follow=True)
        self.assertEqual(resp.status_code, HTTPStatus.OK)


