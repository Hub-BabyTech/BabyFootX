#!/usr/bin/env python3
 
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt 
  
  
# # img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
# # img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
  
  
# # stop_data = cv2.CascadeClassifier('stop_data.xml') 
  
# # found = stop_data.detectMultiScale(img_gray,  
# #                                    minSize =(20, 20)) 
  
# # amount_found = len(found) 
  
# # if amount_found != 0: 
# #     for (x, y, width, height) in found: 
# #         cv2.rectangle(img_rgb, (x, y),  
# #                       (x + height, y + width),  
# #                       (0, 255, 0), 5) 
          
# # img = np.zeros((512,512,3), np.uint8)

# # cv.line(img, (0,0), (511,511), (0,0,255), 5)
# img = cv.imread("images/balloon/one_ballon.png") 

# hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# # cv.circle(img, (100,100), 50, (0,0,255), 3)


# lower_range = np.array([0,0,0])
# upper_range = np.array([0,0,0])

# mask = cv.inRange(hsv, lower_range, upper_range)

# # cv.imshow("Image", img)
# # cv.imshow("Mask", mask)
# # cv.waitKey(0)
# # cv.destroyAllWindows()

# # plt.subplot(1,1,1)
# # plt.imshow(img)
# plt.imshow(mask)
# plt.show()

import cv2
import numpy as np


def detectCirclesWithDp(frame, dp=1):
    blurred = cv2.medianBlur(frame, 25)
    grayMask = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
    # cannyMask = cv2.Canny(grayMask, 50, 240)
    return cv2.HoughCircles(grayMask, cv2.HOUGH_GRADIENT, dp, 40, param1=10, param2=30, minRadius=20, maxRadius=70)

def getROI(frame, x, y, r):
    return frame[int(y-r/2):int(y+r/2), int(x-r/2):int(x+r/2)]


COLOR_NAMES = ["red","green", "blue", "white"]

COLOR_RANGES_HSV = {
    "red": [(0, 50, 10), (10, 255, 255)],
    "green": [(35, 50, 10), (80, 255, 255)],
    "blue": [(100, 50, 10), (130, 255, 255)],
    "white": [(5, 0, 10), (255, 255, 255)]
}

def getMask(frame, color):
    blurredFrame = cv2.GaussianBlur(frame, (3, 3), 0)
    hsvFrame = cv2.cvtColor(blurredFrame, cv2.COLOR_BGR2HSV)

    colorRange = COLOR_RANGES_HSV[color]
    lower = np.array(colorRange[0])
    upper = np.array(colorRange[1])

    colorMask = cv2.inRange(hsvFrame, lower, upper)
    colorMask = cv2.bitwise_and(blurredFrame, blurredFrame, mask=colorMask)

    return colorMask

def getDominantColor(roi):
    roi = np.float32(roi)

    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    K = 4
    ret, label, center = cv2.kmeans(roi, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    center = np.uint8(center)
    res = center[label.flatten()]
    res2 = res.reshape(roi.shape)

    pixelsPerColor = []
    for color in COLOR_NAMES:
        mask = getMask(res2, color)
        greyMask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
        count = cv2.countNonZero(greyMask)
        pixelsPerColor.append(count)

    return COLOR_NAMES[pixelsPerColor.index(max(pixelsPerColor))]

# Read image.
img = cv2.imread('images/stop/color.png', cv2.IMREAD_COLOR)
  
# Convert to grayscale.
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blur using 3 * 3 kernel.
gray_blurred = cv2.blur(gray, (3, 3))

# cv2.imshow('gray_blurred', gray)
# cv2.waitKey(0)
# sys.exit(0)
# Apply Hough transform on the blurred image.
detected_circles = cv2.HoughCircles(gray_blurred, 
                cv2.HOUGH_GRADIENT, 1, 20, param1 = 50,
            param2 = 30, minRadius = 1, maxRadius = 40)

# detected_circles = detectCirclesWithDp(img)

# print("frame", img)
# print(detected_circles)
nb = 1
text = "image : " + str(nb)

img = cv.putText(img, text, (100,100), cv.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv.LINE_AA)

# mycircle = [0, 0, 0]
# Draw circles that are detected.
if detected_circles is not None:
    for circle in detected_circles[0, :]:
        # print(circle[0], circle[1])
            # if imageUtils.inFrame(img, circle[0], circle[1]):
        # print("one circle",circle[0], circle[1], circle[2])
        roi = getROI(img, circle[0], circle[1], circle[2])
        # print(roi)
        color = getDominantColor(roi)
        # print("Color :", color)
        # print("coord : %i %i" % (round(circle[1]), round(circle[0])))
        b, g, r = img[round(circle[1]), round(circle[0])]
        print("Color : %i %i %i" % (r,g,b))
        if r > 200 and g > 200 and b > 200:
            cv2.circle(img, (round(circle[0]), round(circle[1])), round(circle[2]), (0, 255, 0), 2)
        # img[round(circle[1]), round(circle[0])] = [255, 0, 0]
        # if mycircle[2] < round(circle[2]):
        #     mycircle = [round(circle[0]), round(circle[1]), round(circle[2])]
        
        # # IF WANT TO PRINT THE COLOR OF THE CIRCLE
        # cv2.putText(img, color, (int(circle[0] + 20), int(circle[1] + 20)), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
        #                 (0, 255, 255))
cv2.imshow("Detected Circle", img)
# print(mycircle)
cv2.waitKey(0)  



    # # Convert the circle parameters a, b and r to integers.
    # detected_circles = np.uint16(np.around(detected_circles))
  
    # for pt in detected_circles[0, :]:
    #     print("circle", pt)
    #     a, b, r = pt[0], pt[1], pt[2]
  
    #     # Draw the circumference of the circle.
    #     cv2.circle(img, (a, b), r, (0, 255, 0), 2)
  
    #     # Draw a small circle (of radius 1) to show the center.
    #     # cv2.circle(img, (a, b), 1, (0, 0, 255), 3)

# cv2.destroyWindow('frame')