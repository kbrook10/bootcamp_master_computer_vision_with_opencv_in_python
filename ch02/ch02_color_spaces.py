'''
Purpose: Practicing with Color Spaces

'''
##########################################################

# Import necessary libraries
import cv2
import numpy as np

# Load image
img = cv2.imread("../course_materials/Master_OpenCV/images/input.jpg")

# Review the individual color levels
B, G, R = img[0,0]
print(B, G, R)

# Convert the image to grayscale
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(gray_image.shape)


'''
Purpose: Practice converting to HSV

'''
##########################################################

# Load image
img2 = cv2.imread("../course_materials/Master_OpenCV/images/input.jpg")

# Convert image to HSV
hsv_image = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)

# Display the various HSV channels
# cv2.imshow("HSV", hsv_image)
# cv2.imshow("h channel", hsv_image[:,:,0])
# cv2.imshow("s channel", hsv_image[:,:,1])
# cv2.imshow("v channel", hsv_image[:,:,2])


'''
Purpose: Practice converting to RGB

'''
##########################################################

# Load image
img3 = cv2.imread("../course_materials/Master_OpenCV/images/input.jpg")

# Split the image into RGB
B, G, R = cv2.split(img3)

# Display the various BGR indexes
print(B.shape)

# cv2.imshow("B channel", B)
# cv2.imshow("G channel", G)
# cv2.imshow("R channel", R)

# Remake the original channel
merged = cv2. merge([B,G,R])
# cv2.imshow("Merged", merged)

# Enhance the blue of the merged
merged = cv2.merge([B+100, G, R])
# cv2.imshow("Merge w/ Blue Enhanced", merged)


'''
Purpose: Practice creating individual RGB images

'''
##########################################################

# Load image
img4 = cv2.imread("../course_materials/Master_OpenCV/images/input.jpg")

# Create matrix of zeros that match the height and width of the image
zeros = np.zeros(img4.shape[:2], dtype="uint8")

# Display the various images
cv2.imshow("Red", cv2.merge([zeros, zeros, R]))
cv2.imshow("Green", cv2.merge([zeros, G, zeros]))
cv2.imshow("Blue", cv2.merge([B, zeros, zeros]))

# Trigger images and clean up
cv2.waitKey(0)
cv2.destroyAllWindows()
