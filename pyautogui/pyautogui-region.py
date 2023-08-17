import pyautogui

# Capture a specific region: (left, top, width, height)
region_screenshot = pyautogui.screenshot(region=(0, 0, 300, 300))

# Save the screenshot to a file
region_screenshot.save("screenshots/screenshot-pyautogui-region.png")