from art.templatetags.tmpl_extras import random_int

from django.test import TestCase


class ThanksViewTest(TestCase):

    def test_random_int_tag(self):
        r = random_int(1)
        self.assertEqual(r, 1)


