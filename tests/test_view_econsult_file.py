import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    # Initialize the Chrome WebDriver
    driver = webdriver.Chrome()
    # Wait up to 10 seconds for elements to become available
    driver.implicitly_wait(10)
    print(999)
    # Return the WebDriver instance for the test
    yield driver
    # Close the WebDriver instance after the test completes
    driver.quit()

def test_view_eco_file_link(browser):
    # Navigate to the HTML file
    browser.get('/Users/debalinachowdhury/Documents/Afya_Smart_ML_Project/app/templates/view_boneFracture_file.html')  # Replace with the actual file path
    print(1000)
    # Find the link element
    link = browser.find_element_by_tag_name('a')

    # Assert that the link text is 'View eConsult File'
    assert link.text == 'View eConsult File'

    # Assert that clicking the link opens a new tab
    link.click()
    assert len(browser.window_handles) == 2  # Assuming it opens in a new tab

    # You can add more assertions as needed to test the behavior of the link
