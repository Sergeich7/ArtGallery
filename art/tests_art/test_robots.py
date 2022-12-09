from http import HTTPStatus

from django.test import TestCase


class RobotsTest(TestCase):

    def test_absoluteurl_tmplate(self):
        resp = self.client.get('/robots.txt', follow=True)
        self.assertEqual(resp.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(resp, 'robots.txt')
        self.assertEqual(resp["content-type"], "text/plain")
        lines = resp.content.decode().splitlines()
        self.assertEqual(lines[0], "User-agent: *")



