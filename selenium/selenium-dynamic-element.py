from selenium import webdriver
from selenium.webdriver.common.by import By

def test_dynamic_element():
    # Set up the webdriver
    driver = webdriver.Chrome()

    # Maximize the browser window to ensure that it occupies the entire screen
    driver.maximize_window()

    # Direct the driver to navigate to the specified URL
    driver.get('https://ecommerce-playground.lambdatest.io/index.php?route=product/category&path=57')

    # Scroll down till the end
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Locate a specific element on the page using CSS Selector
    specific_element = driver.find_element(By.CSS_SELECTOR, "img[alt='MacBook Air']")

    # Take a screenshot of just the located element and save it to a file
    specific_element.screenshot('screenshots/selenium-dynamic-element.png')

    # Close the browser
    driver.quit()