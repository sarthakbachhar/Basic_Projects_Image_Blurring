import cv2
from matplotlib import pyplot as plt

# Load the image 
img = cv2.imread("C:\\Users\\Acer\\Desktop\\daemon.jpeg")

# Convert image from BGR TO RGB 
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Apply Gaussian Blur 
blurred_image = cv2.GaussianBlur(img_rgb, (3,3), 0)

# Figure to display images
plt.figure(figsize=(10,5))

# For original image
plt.subplot(1,2,1)
plt.imshow(img_rgb)
plt.axis('off')
plt.title("Original Image")

# For blurred image
plt.subplot(1,2,2)
plt.imshow(blurred_image)
plt.axis('off')
plt.title("Gaussian Blurred Image")

# Display both images
plt.show()