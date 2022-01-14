#!/usr/bin/env python3

import cv2
import numpy as np
# import imutils

img = cv2.imread('images/stop/color.png')

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_range = np.array([110,50,50])
upper_range = np.array([130,255,255])

lower_range = np.array([110,50,50])
upper_range = np.array([130,255,255])

mask = cv2.inRange(hsv, lower_range, upper_range)

cnts,hie = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
cv2.drawContours(img,cnts,-1,(0,255,0),3)

cv2.imshow('image', img)
cv2.imshow('mask', mask)

while(True):
   k = cv2.waitKey(5) & 0xFF
   if k == 27:
      break

cv2.destroyAllWindows()