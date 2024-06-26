#loading image in grayscale mode

import cv2
gray_img = cv2.imread('./img/onion.png', cv2.IMREAD_GRAYSCALE)
# used to save the image in the folder
cv2.imwrite('./img/out_onion.png', gray_img)
cv2.imshow('Grayscale', gray_img)
cv2.waitKey()