from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import os
import configparser

# Load the configuration file
config = configparser.ConfigParser()
config.read('config/config.ini')

@pytest.fixture()
def driver(request):
    username = os.getenv("LT_USERNAME")
    config.set('LOGIN', 'username', username)

    accessKey = os.getenv("LT_ACCESS_KEY")
    config.set('LOGIN', 'access_key', accessKey)

    username = config.get('LOGIN', 'username')
    accessKey = config.get('LOGIN', 'access_key')

    gridUrl = config.get('CLOUDGRID', 'grid_url')

    web_driver = webdriver.ChromeOptions()
    platform = config.get('ENV', 'platform')
    browser_name = config.get('ENV', 'browser_name')

    lt_options = {
        "user": config.get('LOGIN', 'username'),
        "accessKey": config.get('LOGIN', 'access_key'),
        "build": config.get('CLOUDGRID', 'build_name'),
        "name": config.get('CLOUDGRID', 'test_name'),
        "platformName": platform,
        "w3c": config.get('CLOUDGRID', 'w3c'),
        "browserName": browser_name,
        "browserVersion": config.get('CLOUDGRID', 'browser_version'),
        "selenium_version": config.get('CLOUDGRID', 'selenium_version'),
		"visual": True
    }

    options = web_driver
    options.set_capability('LT:Options', lt_options)

    url = f"https://{username}:{accessKey}@{gridUrl}"
    
    driver = webdriver.Remote(
        command_executor=url,
        options=options
    )

    yield driver
    
    driver.quit

def test_screenshots_using_lambdatest(driver):
    driver.get(config.get('WEBSITE', 'url'))
       
    # Find an input element by its ID and enter text
    input_element = driver.find_element(By.ID, "user-message")
    input_element.send_keys("This is a screenshot test text!")

    # Find an element by its ID and click on it
    element = driver.find_element(By.ID, "showInput")
    element.click()

    # Find an element by its ID and extract its text
    element = driver.find_element(By.ID, "message")

    assert element.text == "This is a screenshot test text!"