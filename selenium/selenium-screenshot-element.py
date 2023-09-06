from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def test_element():
    # Set up the webdriver
    driver = webdriver.Chrome()

    # Maximize the browser window to ensure that it occupies the entire screen
    driver.maximize_window()

    # Direct the driver to navigate to the specified URL
    driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")

    # Locate a specific element on the page using its ID attribute
    specific_element = driver.find_element(By.ID, "user-message")

    # Take a screenshot of just the located element and save it to a file
    specific_element.screenshot('screenshots/selenium-element-snapshot.png')

    # Close the browser
    driver.quit()