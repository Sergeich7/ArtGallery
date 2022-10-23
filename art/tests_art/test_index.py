from django.test import TestCase
from django.urls import reverse


class IndexViewTest(TestCase):

    def test_index_abs_tmp(self):
        resp = self.client.get('/', follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'art/index.html')

    def test_index_rev(self):
        resp = self.client.get(reverse('art:index'), follow=True)
        self.assertEqual(resp.status_code, 200)


#from django.contrib.auth import get_user_model
#from django.test import Client, TestCase
#from django.urls import reverse
#
#from .models import Post
#
#class BlogTests(TestCase):
#
#    def setUp(self):
#
#        self.user = get_user_model().objects.create_user(
#            username='testuser',
#            email='test@email.com',
#            password='secret',
#        )
#
#        self.post = Post.objects.create(
#            title='A good title',
#            body='Nice body content',
#            author=self.user,
#        )
#
#    def test_sharing_representation(self):
#        post = Post(title='A sample title')
#        self.assertEqual(str(post), post.title)
#
#    def test_get_absolute_url(self):
#        self.assertEqual(self.post.get_absolute_url(), '/post/1')
#
#
#    def test_post_content(self):
#        self.assertEqual(f'{self.post.title}', 'A good title')
#        self.assertEqual(f'{self.post.author}', 'testuser')
#        self.assertEqual(f'{self.post.body}', 'Nice body content')
#
#    def test_post_list_view(self):
#        response = self.client.get(reverse('home'))
#        self.assertEqual(response.status_code, 200)
#        self.assertContains(response, 'Nice body content')
#        self.assertTemplateUsed(response, 'home.html')
#
#    def test_post_detail_view(self):
#        response = self.client.get('/post/1')
#        no_response = self.client.get('/post/1000000')
#        self.assertEqual(response.status_code, 200)
#        self.assertEqual(no_response.status_code, 404)
#        self.assertContains(response, 'A good title')
#        self.assertTemplateUsed(response, 'post_detail.html')
#
#    def test_post_create_view(self):
#        response = self.client.post(reverse('post_new'), {
#            'title': 'New title',
#            'body': 'New title',
#            'author': self.user,
#        })
#        self.assertEqual(response.status_code, 200)
#        self.assertContains(response, 'New title')
#        self.assertContains(response, 'New title')
#
#    def test_post_update_view(self):
#        response = self.client.post(reverse('post_edit', args='1'), {
#            'title': 'Updated title',
#            'body': 'Updated title',
#        })
#        self.assertEqual(response.status_code, 302)
#
#    def test_post_delete_view(self):
#        response = self.client.get(reverse('post_delete', args='1'))
#        self.assertEqual(response.status_code, 200)
#


#import datetime
#
#from django.test import TestCase
#from django.utils import timezone
#from django.urls import reverse
#
#from .models import Question
#
#
#class QuestionModelTests(TestCase):
#
#    def test_was_published_recently_with_future_question(self):
#        """
#        was_published_recently() returns False for questions whose pub_date
#        is in the future.
#        """
#        time = timezone.now() + datetime.timedelta(days=30)
#        future_question = Question(pub_date=time)
#        self.assertIs(future_question.was_published_recently(), False)
#
#    def test_was_published_recently_with_old_question(self):
#        """
#        was_published_recently() returns False for questions whose pub_date
#        is older than 1 day.
#        """
#        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
#        old_question = Question(pub_date=time)
#        self.assertIs(old_question.was_published_recently(), False)
#
#    def test_was_published_recently_with_recent_question(self):
#        """
#        was_published_recently() returns True for questions whose pub_date
#        is within the last day.
#        """
#        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
#        recent_question = Question(pub_date=time)
#        self.assertIs(recent_question.was_published_recently(), True)
#
#
#def create_question(question_text, days):
#    """
#    Create a question with the given `question_text` and published the
#    given number of `days` offset to now (negative for questions published
#    in the past, positive for questions that have yet to be published).
#    """
#    time = timezone.now() + datetime.timedelta(days=days)
#    return Question.objects.create(question_text=question_text, pub_date=time)
#
#
#class QuestionIndexViewTests(TestCase):
#    def test_no_questions(self):
#        """
#        If no questions exist, an appropriate message is displayed.
#        """
#        response = self.client.get(reverse('polls:index'))
#        self.assertEqual(response.status_code, 200)
#        self.assertContains(response, "No polls are available.")
#        self.assertQuerysetEqual(response.context['latest_question_list'], [])
#
#    def test_past_question(self):
#        """
#        Questions with a pub_date in the past are displayed on the
#        index page.
#        """
#        question = create_question(question_text="Past question.", days=-30)
#        response = self.client.get(reverse('polls:index'))
#        self.assertQuerysetEqual(
#            response.context['latest_question_list'],
#            [question],
#        )
#
#    def test_future_question(self):
#        """
#        Questions with a pub_date in the future aren't displayed on
#        the index page.
#        """
#        create_question(question_text="Future question.", days=30)
#        response = self.client.get(reverse('polls:index'))
#        self.assertContains(response, "No polls are available.")
#        self.assertQuerysetEqual(response.context['latest_question_list'], [])
#
#    def test_future_question_and_past_question(self):
#        """
#        Even if both past and future questions exist, only past questions
#        are displayed.
#        """
#        question = create_question(question_text="Past question.", days=-30)
#        create_question(question_text="Future question.", days=30)
#        response = self.client.get(reverse('polls:index'))
#        self.assertQuerysetEqual(
#            response.context['latest_question_list'],
#            [question],
#        )
#
#    def test_two_past_questions(self):
#        """
#        The questions index page may display multiple questions.
#        """
#        question1 = create_question(question_text="Past question 1.", days=-30)
#        question2 = create_question(question_text="Past question 2.", days=-5)
#        response = self.client.get(reverse('polls:index'))
#        self.assertQuerysetEqual(
#            response.context['latest_question_list'],
#            [question2, question1],
#        )
#
#    class QuestionDetailViewTests(TestCase):
#
#        def test_future_question(self):
#            """
#            The detail view of a question with a pub_date in the future
#            returns a 404 not found.
#            """
#            future_question = create_question(question_text='Future question.', days=5)
#            url = reverse('polls:detail', args=(future_question.id,))
#            response = self.client.get(url)
#            self.assertEqual(response.status_code, 404)
#
#        def test_past_question(self):
#            """
#            The detail view of a question with a pub_date in the past
#            displays the question's text.
#            """
#            past_question = create_question(question_text='Past Question.', days=-5)
#            url = reverse('polls:detail', args=(past_question.id,))
#            response = self.client.get(url)
#            self.assertContains(response, past_question.question_text)
#
