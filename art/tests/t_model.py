from django.test import TestCase

from art.models import Category


class CantegoryModelTest(TestCase):

    def setUp(self):
        Category.objects.create(title='just test')

    def test_text_content(self):
        category = Category.objects.get(id=1)
        expected_object_title = f'{category.title}'
        self.assertEqual(expected_object_title, 'just test')
