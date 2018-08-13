'''
Purpose: Convert image post loading

'''
##########################################################

# Import necessary libraries

import cv2
import numpy as np

# Load image
img = cv2.imread("../course_materials/Master_OpenCV/images/input.jpg", 1)

# Convert image to gray
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Display image
cv2.imshow("Image", img)
cv2.imshow("Gray", gray)

'''
Purpose: Convert image on load

'''
##########################################################

# Load image
img_fast = cv2.imread("../course_materials/Master_OpenCV/images/input.jpg", 0)

# Display image
# cv2.imshow("Image", img)
cv2.imshow("Gray_Faster", img_fast)

# Trigger Image and clean up
cv2.waitKey(0)
cv2.destroyAllWindows()