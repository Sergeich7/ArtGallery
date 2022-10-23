from django.test import TestCase
from django.urls import reverse


class ContactViewTest(TestCase):

    def test_contact_abs_tmp(self):
        resp = self.client.get('/contacts/', follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'art/contacts.html')

    def test_contact_rev(self):
        resp = self.client.get(reverse('art:contacts'), follow=True)
        self.assertEqual(resp.status_code, 200)

