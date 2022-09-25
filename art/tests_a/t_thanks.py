from django.test import TestCase
from django.urls import reverse


class ThanksViewTest(TestCase):

    def test_text_content(self):

        resp = self.client.get('/thanks/')
        self.assertEqual(resp.status_code, 200)

        resp = self.client.get(reverse('art:thanks'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'art/thanks.html')


