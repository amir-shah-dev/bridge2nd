from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_view_blog_page(self):

        self.browser.get('http://localhost:8000')

        self.assertIn('My Blog', self.browser.title)

        title = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('My Blog', title)

    def test_redirect_if_not_logged_in(self):
        self.browser.get('http://localhost:8000/post/new/')
        self.assertIn('http://localhost:8000/admin', self.browser.current_url)


class CVEditorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_view_CV_page(self):

        self.browser.get('http://localhost:8000/cv')

        self.assertIn('My Blog', self.browser.title)

    def test_can_edit_CV_page_not_logged_in(self):

        self.browser.get('http://localhost:8000/cv/new/')

        self.assertIn('Log in | Django site admin', self.browser.title)

    def test_redirect_if_not_logged_in(self):
        self.browser.get('http://localhost:8000/cv/new/')
        self.assertIn('http://localhost:8000/admin', self.browser.current_url)

    def get_item_input_box(self):
        return self.browser.find_element_by_id('post-form')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
