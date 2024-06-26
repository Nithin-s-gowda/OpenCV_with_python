import cv2
img = cv2.imread('./img/onion.png')
#convert to grayscal
#gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#convert to YUV
yuv_img = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
cv2.imshow('grayscale image', yuv_img)#change the value 
cv2.waitKey()