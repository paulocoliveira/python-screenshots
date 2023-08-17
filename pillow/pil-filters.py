from PIL import ImageGrab
from PIL import ImageFilter

# Capture the whole screen
img = ImageGrab.grab()

# Apply blur filter to image
blurred_img = img.filter(ImageFilter.BLUR)

# Display the image
blurred_img.show()

# Save the image to file
blurred_img.save("screenshots/screenshot-filters.png")