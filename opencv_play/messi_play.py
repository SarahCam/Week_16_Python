import cv2
import numpy

img = cv2.imread("messi.jpg")
# print(img)

# Point 1: 360, 280
# Point 2: 410, 330
# [y1:y2, x1:x2]

# assign section to ball
ball = img[280:330, 360:410]

# make a section of img be replaced by ball image
img[180:230, 260:310] = ball

cv2.imwrite("messi-modified.jpg", img)
