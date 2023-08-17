from PIL import ImageGrab

# Capture the whole screen
img = ImageGrab.grab()

# Define the cropping box
box = (50, 50, 250, 250)
cropped_img = img.crop(box)

# Display the image
cropped_img.show()

# Save the image to file
cropped_img.save("screenshots/screenshot-cropping.png")