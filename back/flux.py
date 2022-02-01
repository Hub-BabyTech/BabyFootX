#!/usr/bin/python3
import cv2

cam = cv2.VideoCapture(0)

nom_fenetre = "webcam"

l_i = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
h_i = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

cv2.namedWindow(nom_fenetre, cv2.WND_PROP_FULLSCREEN)

face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
	ret, image = cam.read()

	if ret:
		found = face_data.detectMultiScale(image, minSize =(20, 20))
		amount_found = len(found)
		if amount_found != 0:
			for (x, y, width, height) in found:
				cv2.rectangle(image, (x, y), (x + height, y + width), (0, 255, 0), 5)
		cv2.imshow(nom_fenetre, image)
		if cv2.waitKey(25) & 0xFF == ord('q'):
			break