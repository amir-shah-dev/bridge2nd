from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_view_blog_page(self):

        self.browser.get('http://localhost:8000')

        self.assertIn('My Blog', self.browser.title)
        # self.fail('Finish the test!')

        first_post_title = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('1st post', first_post_title)
        first_post_text = self.find_element_by_tag_name('p').text
        self.assertIn('Is it working?', first_post_text)


class CVEditorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_view_CV_page(self):

        self.browser.get('http://localhost:8000')

        self.assertIn('My Blog', self.browser.title)

        page_header = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('My CV', page_header)

        # Include more tests to ensure that the page is visible


    # def test_can_edit_page(self):

if __name__ == '__main__':
    unittest.main(warnings='ignore')

# browser = webdriver.Firefox()
# browser.get('http://localhost:8000')

# assert 'Django' in browser.title
