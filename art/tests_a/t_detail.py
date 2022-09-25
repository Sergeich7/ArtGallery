from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from art.models import Category, Author, Technique, Product, ArtComment


class DetailViewTest(TestCase):

    def setUp(self):
        Author.objects.create(last_name='just Author')
        Category.objects.create(title='just Category')
        Technique.objects.create(title='just Technique')
        Product.objects.create(title='just Product', author_id=1, category_id=1, technique_id=1)
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret',
        )
        ArtComment.objects.create(text='just ArtComment', product_id=1, user=self.user)

    def test_text_content(self):
        tst_obj = Category.objects.get(id=1)
        expected_object_field = f'{tst_obj.title}'
        self.assertEqual(expected_object_field, 'just Category')

        tst_obj = Author.objects.get(id=1)
        expected_object_field = f'{tst_obj.last_name}'
        self.assertEqual(expected_object_field, 'just Author')

        tst_obj = Technique.objects.get(id=1)
        expected_object_field = f'{tst_obj.title}'
        self.assertEqual(expected_object_field, 'just Technique')

        tst_prod = Product.objects.get(id=1)
        expected_object_field = f'{tst_prod.title}'
        self.assertEqual(expected_object_field, 'just Product')

        tst_obj = ArtComment.objects.get(id=1)
        expected_object_field = f'{tst_obj.text}'
        self.assertEqual(expected_object_field, 'just ArtComment')

        resp = self.client.get('/1/')
        self.assertEqual(resp.status_code, 200)

        resp = self.client.get(reverse('art:detail', args=[1]))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'art/detail.html')

