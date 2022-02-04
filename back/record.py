#!/usr/bin/python3
import cv2

cam = cv2.VideoCapture("../fifo264")

nom_fenetre = "webcam"

cv2.namedWindow(nom_fenetre, cv2.WND_PROP_FULLSCREEN)

nb = 0

width= int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
height= int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

writer= cv2.VideoWriter('new.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 20, (width,height))

while True:
	ret, image = cam.read()

	if ret:
		writer.write(image)
		text = "image : " + str(nb)
		cv2.putText(image, text, (100,100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv2.LINE_AA)
		cv2.imshow(nom_fenetre, image)
		if cv2.waitKey(25) & 0xFF == ord('q'):
			break
	nb +=1