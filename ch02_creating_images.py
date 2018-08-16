'''
Purpose:
~ Create an image that is all black in color and in b/w
'''

# Import libraries
import cv2
import numpy as np 

# Create black image in color
'''
(512, 512,3) -> width, height, channels
np.uint8 -> data type 0 to 255 pixel
'''
image = np.zeros((512,512,3), np.uint8)

# Create black image in b/w
image_bw = np.zeros((512,512), np.uint8)

# Display the images
cv2.imshow("Black image in Color", image)
cv2.imshow("Black image in Black/White", image_bw)





'''
Purpose:
~ Draw a line across an image
'''

# Create image
image2 = np.zeros((512,512,3), np.uint8)

# Create line
'''
(0,0) -> line start point
(511,511) -> line end point
(255,127,0) -> line color
5 -> line thickness
''' 
cv2.line(image2,(0,0), (511,511), (255,127,0), 5)

# Display image with Blue Line
cv2.imshow("Blue Line", image2)

'''
Purpose:
~ Draw a rectangle across an image
'''

# Create image
image3 = np.zeros((512,512,3), np.uint8)

# Create Rectangle
'''
(100,100) -> line start point
(300,250) -> line end point
(127,50,127) -> line color
5 -> line thickness
'''
cv2.rectangle(image3, (100,100), (300,250), (127,50,127), 5)

# Display image with rectangle
cv2.imshow("Rectangle", image3)

'''
Purpose:
~ Draw a rectangle across an image
'''

# Create image
image3 = np.zeros((512,512,3), np.uint8)

# Create Rectangle
'''
(100,100) -> line start point
(300,250) -> line end point
(127,50,127) -> line color
5 -> line thickness
'''
cv2.rectangle(image3, (100,100), (300,250), (127,50,127), 5)

# Display image with rectangle
cv2.imshow("Rectangle", image3)


# Trigger image and clean up
cv2.waitKey(0)
cv2.destroyAllWindows()