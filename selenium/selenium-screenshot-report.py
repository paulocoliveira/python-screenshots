from selenium import webdriver
from selenium.webdriver.common.by import By

def test_report():
    # Set up the webdriver
    driver = webdriver.Chrome()

    # Maximize the browser window to ensure that it occupies the entire screen
    driver.maximize_window()

    # Direct the driver to navigate to the specified URL
    driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")

    try:
        # Find an element by its ID and click on it
        element = driver.find_element(By.ID, "showInput")
        element.click()
    except Exception as e:
        driver.get_screenshot_as_file("test_failure.png")
        raise e  # Rethrow the exception to mark the test as failed

    # Close the browser
    driver.quit()