from http import HTTPStatus

from django.test import TestCase


class ThanksViewTest(TestCase):
    def test_robots_abs_tmp(self):
        resp = self.client.get('/robots.txt', follow=True)
        self.assertEqual(resp.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(resp, 'robots.txt')
        self.assertEqual(resp["content-type"], "text/plain")
        lines = resp.content.decode().splitlines()
        self.assertEqual(lines[0], "User-agent: *")
        resp = self.client.post("/robots.txt")
        self.assertEqual(resp.status_code, HTTPStatus.METHOD_NOT_ALLOWED)



