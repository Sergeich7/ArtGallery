from django.test import TestCase
from django.urls import reverse


class ContactViewTest(TestCase):

    def test_text_content(self):

        resp = self.client.get('/contacts/')
        self.assertEqual(resp.status_code, 200)

        resp = self.client.get(reverse('art:contacts'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'art/contacts.html')

