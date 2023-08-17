from PIL import ImageGrab

# Capture the whole screen
img = ImageGrab.grab()

# Display the image
img.show()

# Save the image to file
img.save("screenshots/screenshot-entire-screen.png")
