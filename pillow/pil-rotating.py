from PIL import ImageGrab

# Capture the whole screen
img = ImageGrab.grab()

# Rotates the image by 90 degrees
rotated_img = img.rotate(90) 

# Display the image
rotated_img.show()

# Save the image to file
rotated_img.save("screenshots/screenshot-rotating.png")