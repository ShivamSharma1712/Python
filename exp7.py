import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image (replace with a valid image path if not using Google Colab)
image = cv2.imread("C:/Users/hp/Downloads/doc1.jpg")


# Check if image is loaded properly
if image is None:
    raise ValueError("Image not found. Please check the path.")

# Convert BGR to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Convert BGR to Grayscale
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Create a white image
white_image = np.ones((300, 300, 3), dtype=np.uint8) * 255

# Create a black image
black_image = np.zeros((300, 300, 3), dtype=np.uint8)

# Copy the original image to draw shapes
image_shapes = image.copy()

# Draw a red rectangle
cv2.rectangle(image_shapes, (50, 50), (200, 200), (0, 0, 255), 3)

# Draw a green filled circle
cv2.circle(image_shapes, (300, 300), 50, (0, 255, 0), -1)

# Draw a blue line
cv2.line(image_shapes, (0, 0), (400, 400), (255, 0, 0), 2)

# Convert image_shapes to RGB for matplotlib display
image_shapes_rgb = cv2.cvtColor(image_shapes, cv2.COLOR_BGR2RGB)

# Display using matplotlib
plt.figure(figsize=(16, 10))
plt.subplot(2, 3, 1)
plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis("off")

plt.subplot(2, 3, 2)
plt.imshow(image_gray, cmap='gray')
plt.title("Grayscale Image")
plt.axis("off")

plt.subplot(2, 3, 3)
plt.imshow(white_image)
plt.title("White Image")
plt.axis("off")

plt.subplot(2, 3, 4)
plt.imshow(black_image)
plt.title("Black Image")
plt.axis("off")

plt.subplot(2, 3, 5)
plt.imshow(image_shapes_rgb)
plt.title("Image with Shapes")
plt.axis("off")

plt.tight_layout()
plt.show()
