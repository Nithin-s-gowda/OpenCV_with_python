#Reading, displaying, and saving images
import cv2
img = cv2.imread('./img/car1.jpg')
cv2.imshow('Input image', img)
cv2.waitKey()