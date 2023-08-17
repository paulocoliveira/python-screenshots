import pygetwindow as gw
import pyautogui

# Get a specific window by its title
window = gw.getWindowsWithTitle('Calculadora')[0]

# Use PyAutoGUI to capture the window's region
screenshot = pyautogui.screenshot(region=(window.left, window.top, window.width, window.height))
screenshot.save("screenshots/screenshot-application-window.png")