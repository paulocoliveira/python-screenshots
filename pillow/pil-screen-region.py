from PIL import ImageGrab

# Define the region (left, top, right, bottom). This captures a 300x300 box from the top-left corner.
region = (0, 0, 300, 300)
img_region = ImageGrab.grab(bbox=region)

# Display the image
img_region.show()

# Save the image to file
img_region.save("screenshots/screenshot-region.png")