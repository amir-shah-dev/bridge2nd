from django.test import TestCase
from django.urls import resolve
from blog.views import post_list

# Create your tests here.


# class SmokeTest(TestCase):

#     def test_bad_maths(self):
#         self.assertEqual(1 + 1, 3)


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, post_list)
