import cv2
import numpy as np

# Global variables
drawing = False  # Flag to indicate whether drawing is in progress
radius = 10      # Radius of the drawing circle (adjust as needed)

# Function to draw on the image
def draw_circle(event, x, y, flags, param):
    global drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            # Draw a white circle on the image at the mouse position
            cv2.circle(img, (x, y), radius, (255, 255, 255), -1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False

# Create a window to display the webcam feed
cv2.namedWindow('Webcam Drawing')

# Set the mouse callback function for the window
cv2.setMouseCallback('Webcam Drawing', draw_circle)

# Open a connection to the webcam (use 0 for the default camera)
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame from the webcam
    ret, frame = cap.read()

    # Create an empty image for drawing
    img = np.zeros_like(frame)

    # Display the frame with the drawing overlay
    cv2.imshow('Webcam Drawing', frame + img)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
