import pyautogui

# Capture the entire screen
screenshot = pyautogui.screenshot()

# Save the screenshot to a file
screenshot.save("screenshots/screenshot-pyautogui-screen.png")