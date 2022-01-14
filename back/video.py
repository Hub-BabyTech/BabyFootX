#!/usr/bin/env python3

import sys
import time
# from tkinter.tix import Balloon
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt 

start_time = time.time()

def detectCirclesWithDp(frame, dp=1):
    blurred = cv.medianBlur(frame, 25)
    grayMask = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)
    # cannyMask = cv2.Canny(grayMask, 50, 240)
    return cv.HoughCircles(grayMask, cv.HOUGH_GRADIENT, dp, 40, param1=10, param2=30, minRadius=20, maxRadius=70)

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
    blurredFrame = cv.GaussianBlur(frame, (3, 3), 0)
    hsvFrame = cv.cvtColor(blurredFrame, cv.COLOR_BGR2HSV)

    colorRange = COLOR_RANGES_HSV[color]
    lower = np.array(colorRange[0])
    upper = np.array(colorRange[1])

    colorMask = cv.inRange(hsvFrame, lower, upper)
    colorMask = cv.bitwise_and(blurredFrame, blurredFrame, mask=colorMask)

    return colorMask

def getDominantColor(roi):
    roi = np.float32(roi)

    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    K = 4
    ret, label, center = cv.kmeans(roi, K, None, criteria, 10, cv.KMEANS_RANDOM_CENTERS)

    center = np.uint8(center)
    res = center[label.flatten()]
    res2 = res.reshape(roi.shape)

    pixelsPerColor = []
    for color in COLOR_NAMES:
        mask = getMask(res2, color)
        greyMask = cv.cvtColor(mask, cv.COLOR_BGR2GRAY)
        count = cv.countNonZero(greyMask)
        pixelsPerColor.append(count)

def displayPicture(img, nb, balloon):
    img[0:100,0:100] = [0,0,0]
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
  
    # Blur using 3 * 3 kernel.
    gray_blurred = cv.blur(gray, (3, 3))
    
    # Apply Hough transform on the blurred image.
    detected_circles = cv.HoughCircles(gray_blurred, 
                    cv.HOUGH_GRADIENT, 1, 20, param1 = 50,
                param2 = 30, minRadius = 1, maxRadius = 40)
    # print("frame", img)
    # print(detected_circles)
    # mycircle = [0, 0, 0]

    text = "image : " + str(nb)

    cv.putText(img, text, (100,100), cv.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv.LINE_AA)
    newBalloon = []
    size = 0
    # Draw circles that are detected.
    if detected_circles is not None:

        # Convert the circle parameters a, b and r to integers.
        detected_circles = np.uint16(np.around(detected_circles))
    
        size = 0
        # print(len(detected_circles))
        for pt in detected_circles[0, :]:
            a, b, r = pt[0], pt[1], pt[2]
    
            # roi = getROI(img, pt[0], pt[1], pt[2])
            # color = getDominantColor(roi)

            # Draw the circumference of the circle.
            # if color == "white":
            # b, g, r = int(img[round(pt[0]), round(pt[1])])
            # print("Color : %i %i %i" % (r,g,b))
            b, g, r = img[round(pt[1]), round(pt[0])]
            # print("Color : %i %i %i" % (r,g,b))
            if r > 150 and g > 150 and b > 150 and pt[2] > 25:
              cv.circle(img, (round(pt[0]), round(pt[1])), round(pt[2]), (0, 255, 0), 2)
              newBalloon += [round(pt[0]), -round(pt[1])]
              size += 1
        
            # cv.putText(img, color, (int(a + 20), int(b + 20)), cv.FONT_HERSHEY_SIMPLEX, 0.5,
            #             (0, 255, 255))
            # if mycircle[2] < round(pt[2]):
              # mycircle = [round(pt[0]), round(pt[1]), round(pt[2])]
    
            # Draw a small circle (of radius 1) to show the center.
            # cv2.circle(img, (a, b), 1, (0, 0, 255), 3)
            # cv.circle(img, (mycircle[0], mycircle[1]), mycircle[2], (0, 255, 0), 2)
    if size > 1:
        print(size, nb)
    cv.imshow("Detected Circle", img)
    # sys.exit(0)
    return balloon+newBalloon, nb+1


# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
cap = cv.VideoCapture('images/videos/60fps/04.mp4')

# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video stream or file")
nb = 1
balloon = []
# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
#   print("frame", frame)
  if ret == True:

    # Display the resulting frame
    balloon, nb = displayPicture(frame, nb, balloon)
    # cv.imshow('Frame',frame)

    # Press Q on keyboard to  exit
    if cv.waitKey(1) & 0xFF == ord('q'):
      break

  # Break the loop
  else: 
    break

# When everything done, release the video capture object
cap.release()
print('--- %s seconds ---' % (time.time() - start_time))
print(balloon)

# Closes all the frames
cv.destroyAllWindows()

f = open("data.txt", "r+")
for i in balloon:
  f.write(str(i) + "\n")
f.close()