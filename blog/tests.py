from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from blog.views import post_list

# Create your tests here.


# class SmokeTest(TestCase):

#     def test_bad_maths(self):
#         self.assertEqual(1 + 1, 3)


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
