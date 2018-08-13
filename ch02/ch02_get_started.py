'''
Purpose: Load and Display an image

'''
##########################################################

# Import necessary libraries

import cv2
import numpy as np

# Load image

img = cv2.imread("../course_materials/Master_OpenCV/images/input.jpg")

# Display image

cv2.imshow("Image", img)

# Trigger Image and clean up

cv2.waitKey(0)
cv2.destroyAllWindows()


'''
Purpose: Reviewing how images are stored

'''
##########################################################



# Print the shape of the image
print(img.shape)

# Display image properties

print("Height of the Image: {} pixels".format(int(img.shape[0])))
print("Width of the Image: {} pixels".format(int(img.shape[1])))

'''
Purpose: Save an image

'''
##########################################################

# Save image
cv2.imwrite('output.jpg', img)