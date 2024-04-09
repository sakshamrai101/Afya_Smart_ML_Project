from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class TestTargetedQuestionsPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test_display_of_targeted_questions(self):

        driver = self.driver
        driver.get("http://127.0.0.1:2222/Targeted_questions")

        question_list = driver.find_element(By.CLASS_NAME, 'question-list')
        questions = question_list.find_elements(By.TAG_NAME, 'li')

        self.assertTrue(len(questions) > 0, "No questions are displayed.")

    def test_done_button_click(self):
        """
        Test that clicking the 'Done' button navigates to the correct URL or triggers the right action.
        """
        driver = self.driver
        driver.get("http://localhost:5000/path_to_targeted_questions_page")

        done_button = driver.find_element(By.ID, 'doneButton')
        done_button.click()

        self.assertEqual(driver.current_url, "http://127.0.0.1:2222/operation3")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
