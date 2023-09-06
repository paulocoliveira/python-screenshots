from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def test_fullpage():
    # Set up the webdriver
    driver = webdriver.Chrome()

    # Maximize the browser window to ensure that it occupies the entire screen
    driver.maximize_window()

    # Direct the driver to navigate to the specified URL
    driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")

    # Take a screenshot of the entire webpage and save it to a file in the specific path
    driver.save_screenshot('screenshots/selenium-save-screenshot.png')

    # Take a screenshot of the entire webpage and save it to a file
    driver.get_screenshot_as_file('screenshots/selenium-get-screenshot-as-file.png')

    # Take a screenshot of the entire webpage and save the data that can be used for further processing or saving
    screenshot_data = driver.get_screenshot_as_png()

    # Close the browser
    driver.quit()
