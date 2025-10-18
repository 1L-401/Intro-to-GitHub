# hello_image.py
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Display Hello World in console
print("Hello, World!")

# Load and display the image
img = mpimg.imread('example.jpg')
plt.imshow(img)
plt.axis('off')  # Hide axes
plt.show()
