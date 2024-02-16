# Importing OpenCV package 
import cv2 

# Reading the image 
#img = cv2.imread('Photos/cric4.jpg') 
cap = cv2.VideoCapture(0)
cap.set(10, 150)

while True: 

	# Read a frame from the webcam
	ret, frame = cap.read() 
	if not ret: 
		print('Image not captured') 
		break
	# Loading the required haar-cascade xml classifier file 
	haar_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 
	# Applying the face detection method on the grayscale image 
	faces_rect = haar_cascade.detectMultiScale(frame, 1.1, 9) 
	# Iterating through rectangles of detected faces 
	for (x, y, w, h) in faces_rect: 
		cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
	cv2.imshow('Detected faces', frame) 
	cv2.waitKey(0) 
	cap.release() 
	cv2.destroyAllWindows()
