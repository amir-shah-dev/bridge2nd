from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.contrib.auth.models import User

from http import HTTPStatus

from blog.views import post_list, cv_list
from blog.forms import PostForm, CVForm, EMPTY_TEXT_ERROR, EMPTY_TITLE_ERROR

# Create your tests here.


class HomePageTest(TestCase):

    def setUp(self):
        test_user1 = User.objects.create_user(username='testuser1', password='3458dshjkghyyf4!')
        test_user1.save()

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, post_list)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = post_list(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('\n'))
        self.assertIn('<title>My Blog</title>', html)
        self.assertTrue(html.endswith('</html>'))

    def test_post_form_validation_for_blank_text_items(self):
        form = PostForm(data={'text': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['text'], [EMPTY_TEXT_ERROR])

    def test_post_form_validation_for_blank_title_items(self):
        form = PostForm(data={'title': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['title'], [EMPTY_TITLE_ERROR])

    def test_post_new_page_uses_form(self):
        login = self.client.login(username='testuser1', password='3458dshjkghyyf4!')
        response = self.client.get('/post/new/')
        self.assertIsInstance(response.context['form'], PostForm)

    def test_redirect_if_not_logged_in(self):
        response = self.client.get('/post/new/')
        self.assertEqual(response.status_code, 302)
        self.assertIn('/admin', response.url)

    def test_logged_in_uses_correct_template(self):
        login = self.client.login(username='testuser1', password='3458dshjkghyyf4!')
        response = self.client.get('/post/new/')

        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'blog/post_edit.html')



class CVPageTest(TestCase):

    def setUp(self):
        test_user1 = User.objects.create_user(username='testuser1', password='3458dshjkghyyf4!')
        test_user1.save()

    def test_cv_url_resolves_to_CV_page(self):
        found = resolve('/cv')
        self.assertEqual(found.func, cv_list)

    def test_cv_page_returns_correct_html(self):
        response = self.client.get('/cv')
        self.assertTemplateUsed(response, 'blog/base.html')
        self.assertTemplateUsed(response, 'blog/cv_list.html')

    def test_cv_form_validation_for_blank_text_items(self):
        form = CVForm(data={'text': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['text'], [EMPTY_TEXT_ERROR])

    def test_cv_form_validation_for_blank_title_items(self):
        form = CVForm(data={'title': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['title'], [EMPTY_TITLE_ERROR])

    def test_cv_new_page_uses_form(self):
        login = self.client.login(username='testuser1', password='3458dshjkghyyf4!')
        response = self.client.get('/cv/new/')
        self.assertIsInstance(response.context['form'], CVForm)

    def test_redirect_if_not_logged_in(self):
        response = self.client.get('/cv/new/')
        self.assertEqual(response.status_code, 302)
        self.assertIn('/admin', response.url)

    def test_logged_in_uses_correct_template(self):
        login = self.client.login(username='testuser1', password='3458dshjkghyyf4!')
        response = self.client.get('/cv/new/')

        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'blog/post_edit.html')
