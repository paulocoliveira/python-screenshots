# Import necessary modules from the selenium package
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Initialize a Chrome Driver Service
service = Service()

# Create an instance of ChromeOptions which will allow you to set options for the Chrome driver
options = webdriver.ChromeOptions()

# Initialize the Chrome driver with the specified service and options
driver = webdriver.Chrome(service=service, options=options)

# Maximize the browser window to ensure that it occupies the entire screen
driver.maximize_window()

# Direct the driver to navigate to the specified URL
driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")

# Take a screenshot of the entire webpage and save it to a file
driver.get_screenshot_as_file('screenshots/selenium-fullpage-snapshot.png')

# Locate a specific element on the page using its ID attribute
specific_element = driver.find_element(By.ID, "user-message")

# Take a screenshot of just the located element and save it to a file
specific_element.screenshot('screenshots/element-snapshot.png')