from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse


class ContactTest(TestCase):

    def test_absoluteurl_tmplate(self):
        resp = self.client.get('/contacts/', follow=True)
        self.assertEqual(resp.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(resp, 'art/contacts.html')

    def test_reverseurl(self):
        resp = self.client.get(reverse('art:contacts'), follow=True)
        self.assertEqual(resp.status_code, HTTPStatus.OK)

