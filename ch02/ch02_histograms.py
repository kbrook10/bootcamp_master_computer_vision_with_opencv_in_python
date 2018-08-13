'''
Purpose: Practicing with Histograms to show dominant colors

'''
##########################################################

# Import necessary libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt


# Load image
img = cv2.imread("../course_materials/Master_OpenCV/images/input.jpg")

# Create histogram of image
histogram = cv2.calcHist([img], [0], None, [256], [0,256])

# Flaten out the image
plt.hist(img.ravel(), 256, [0,256])

# Plot the image
plt.show()

# View each channel separately on the histogram
color = ('b', 'g', 'r')

# Separate the colors and plot
for i, col in enumerate(color):
	histogram2 = cv2.calcHist([img],[i],None, [256], [0,256])
	plt.plot(histogram2,color*col)
	plt.xlim([0.256])

plt.show()