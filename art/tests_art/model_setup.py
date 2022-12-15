from django.contrib.auth import get_user_model

from art.models import Category, Author, Technique, Product, ArtComment


class ModelSetupMixin():

    def setUp(self):
        """Наполняем данными тестовую модель."""
        a = Author.objects.create(
            last_name='just Author', first_name='just Author', slug='just1aut')
        c = Category.objects.create(title='just Category', slug='just1cat')
        t = Technique.objects.create(title='just Technique', slug='just1tec')
        p = Product.objects.create(
            title='just Product', description='just Description', price=1000, slug='just1product', author=a, category=c,
            technique=t)
        th = p.images.create(picture="picname.jpg")
        p.thumb_of_day = th.picture
        p.save()
        u = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret',
        )
        self.prod1 = p
        ArtComment.objects.create(text='just ArtComment', product=p, user=u)

