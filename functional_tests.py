import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class HomePageTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_website_is_active(self):

        self.browser.get('http://loneelder.com')

        self.assertIn("Lone Elder", self.browser.title)

        description_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('nursery', description_text)

    def test_search_by_name_returns_valid_results(self):

        self.browser.get('http://loneelder.com')

        inputbox = self.browser.find_element_by_id('SearchString')
        self.assertEqual(inputbox.get_attribute('value'),
                         'Search by name')
        inputbox.clear()
        inputbox.send_keys('abies')
        inputbox.send_keys(Keys.ENTER)

        #import time; time.sleep(3)

        row = self.browser.find_element_by_css_selector("tr.OddRow")
        cells = row.find_elements_by_tag_name('td')
        self.assertIn('Abies', [cell.text for cell in cells])

if __name__ == '__main__':
    unittest.main(warnings='ignore')
    