"""
This file consist of the basics of the opencv library along with
basic functionality like reading an image and video and resizing
"""
import cv2

def reading_writing():
    """ Part 1- Opencv basics - reading and writing an image file"""
    
    image = cv2.imread('/home/unthinkable-lap/Pictures/screen.png')
    cv2.imshow('Image is here', image)
    resized_image = cv2.resize(image, (300, 300))
    cv2.imshow('resized image', resized_image)
    cv2.imwrite('resized_image.jpg', resized_image)
    cv2.waitKey(0)
    print("Reading and writing of data is done in this")

