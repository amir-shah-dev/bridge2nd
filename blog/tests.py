from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from http import HTTPStatus

from blog.views import post_list, cv_list
from blog.forms import PostForm, CVForm, EMPTY_TEXT_ERROR, EMPTY_TITLE_ERROR

# Create your tests here.


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, post_list)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = post_list(request)
        html = response.content.decode('utf8')
        # print(html)
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


class CVPageTest(TestCase):

    def test_cv_url_resolves_to_CV_page(self):
        found = resolve('/cv')
        self.assertEqual(found.func, cv_list)

    def test_cv_page_returns_correct_html(self):
        # request = HttpRequest()
        response = self.client.get('/cv')
        # html = response.content.decode('utf8')
        self.assertTemplateUsed(response, 'blog/base.html')
        self.assertTemplateUsed(response, 'blog/cv_list.html')
        # self.assertIn('1st section', html)

    # def test_can_save_post(self):
    #     response = self.client.post('/cv/new', data={'title': 'This is a func test'})
    #     # self.assertIn('This is a func test', response.content.decode())
    #     # self.assertEqual(response.status_code, HTTPStatus.FOUND)
    #     self.assertEqual(response["Location"], "/cv/")

    def test_cv_form_validation_for_blank_text_items(self):
        form = CVForm(data={'text': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['text'], [EMPTY_TEXT_ERROR])

    def test_cv_form_validation_for_blank_title_items(self):
        form = CVForm(data={'title': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['title'], [EMPTY_TITLE_ERROR])

    # def test_cv_page_uses_form(self):
    #     response = self.client.get('/cv')
    #     self.assertIsInstance(response.context['form'], CVForm)

