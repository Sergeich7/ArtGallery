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

    def test_send_mail_wtih_valid_data(self):
        resp = self.client.post(
            '/contacts/',
            {
                'to': 'adm',
                'name': 'test',
                'email': 'test@test.ru',
                'message': 'test',
                'captcha_0': 'dummy-value',
                'captcha_1': 'PASSED',
            }, follow=True)
        self.assertRedirects(resp, reverse('art:thanks'))
