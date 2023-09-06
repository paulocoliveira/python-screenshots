import json
import requests
import os
from time import sleep

# API documentation: https://www.lambdatest.com/support/docs/automated-screenshot-api-for-cross-browser-testing/

username = os.getenv("LT_USERNAME")
accessKey = os.getenv("LT_ACCESS_KEY")

def test_screenshot_api():
    url = "https://%s:%s@api.lambdatest.com/screenshots/v1" % (username, accessKey)
    headers = {"accept": "application/json", "Content-Type": "application/json"}
    payload = {
        "url": "https://www.lambdatest.com/selenium-playground/simple-form-demo",
        "defer_time": 5,
        "email": True,
        "mac_res": "1024x768",
        "win_res": "1366X768",
        "configs": {
            "windows 10": {
                "chrome": ["74"],
                "firefox": ["66"],
                "opera": ["58"],
                "ie": ["11"]
            },
            "macos mojave": {
                "chrome": ["74"]
            }
        }
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    assert response.status_code == 200
    response_data = response.json()
    test_id = response_data.get('test_id')  # Using `get` method to avoid KeyError if 'test_id' is not present.
    print(f"The test ID is: {test_id}")
    sleep(45)
    fetch_details_executed_test_session(test_id)

def fetch_details_executed_test_session(testId):
    url = "https://%s:%s@api.lambdatest.com/screenshots/v1/%s" % (username, accessKey, testId)
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    response_data = response.json()
    print(response_data)

