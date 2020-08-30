from django.test import TestCase
from selenium import webdriver


class Funtionaltest(TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def test_there_is_homepage(self):
        self.browser.get('http://localhost:8000/')
        self.assertIn('PORTFOLIO',self.browser.page_source)
        self.assertIn('BLOG',self.browser.page_source)


    def test_there_is_Introduction(self):
        self.browser.get('http://localhost:8000/base/home.html')
        self.assertIn('Introduction',self.browser.page_source)

    def test_there_is_Projects(self):
        self.browser.get('http://localhost:8000/base/home.html')
        self.assertIn('Project',self.browser.page_source)

    def test_there_is_Projects(self):
        self.browser.get('http://localhost:8000/base/home.html')
        self.assertIn('Flappy bird using ai',self.browser.page_source)

    def test_there_is_Projects(self):
        self.browser.get('http://localhost:8000/base/home.html')
        self.assertIn('Maze solving Bot',self.browser.page_source)

    def test_there_is_Projects(self):
        self.browser.get('http://localhost:8000/base/home.html')
        self.assertIn('Bitcoin price tracker app',self.browser.page_source)

    def test_there_is_Projects(self):
        self.browser.get('http://localhost:8000/base/home.html')
        self.assertIn('live sketch',self.browser.page_source)

    def test_there_is_Skills(self):
        self.browser.get('http://localhost:8000/base/home.html')
        self.assertIn('Skills',self.browser.page_source)

    def test_there_is_Achievements(self):
        self.browser.get('http://localhost:8000/base/home.html')
        self.assertIn('Achievements',self.browser.page_source)

    def tearDown(self):
        self.browser.quit()

class Unittest(TestCase):
        def test_there_is_mainpage(self):
            response = self.client.get('/')
            self.assertTemplateUsed(response,'base/main.html')
