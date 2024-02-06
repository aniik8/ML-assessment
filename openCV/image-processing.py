"""
Image processing techniques involve manipulating 
images to enhance their quality, extract useful 
information, or prepare them for further analysis.
"""
import cv2
import numpy as np
def blurr_processing():
    """
    Blurring reduces the noise in an image by averaging 
    the pixel values in a neighborhood.
    """
    image = cv2.imread('images.jpeg')
    #cv2.imshow('Image shown', image) 
    #The cv2.blur()  - simple averaging over
    #a specified kernel, which helps to blur the image.  
    blurred_image = cv2.blur(image, (50, 10))


    # (ksize_x, ksize_y): Size of the Gaussian kernel.
    #It should be an odd integer.
    #sigma_x: Standard deviation of the Gaussian kernel along the x-axis. 
    #
    # If set to 0, it is calculated from the kernel size.
    blurred_gaussian = cv2.GaussianBlur(image, (5, 1), 0)

    #ksize(the number below): Size of the kernel. It should be a positive odd integer.
    
    blurred_median = cv2.medianBlur(image, 9)
    cv2.imshow('Image blurr', blurred_image)
    cv2.imshow('Image gaussian', blurred_gaussian)
    cv2.imshow('Image median', blurred_median)
    cv2.waitKey(0)

#blurr_processing()

def image_sharpening():

    image = cv2.imread('images.jpeg')

    laplacian = cv2.Laplacian(image, cv2.CV_64F)
    #it make sure image lies between 0-255 pixel range
    sharpened_image = np.uint8(np.clip(image - 0.5*laplacian, 0, 255))
    cv2.imshow('Sharpened image', sharpened_image)
    cv2.waitKey(0)

#image_sharpening()

#Image thresholding -- is used to convert grayscale image to binary classification black and \
#white image

def thresholding():
    image = cv2.imread('images.jpeg')
    threshold_value = 128
    max_value = 255
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    ret, thresholded_image = cv2.threshold(gray_image, threshold_value, max_value, cv2.THRESH_TOZERO_INV)
    cv2.imshow("Original image", image)
    cv2.imshow("threshold image", thresholded_image)
    cv2.waitKey(0)
#thresholding()

#edge detection of an image
def edge_detection():
    image = cv2.imread('images.jpeg')
    gray_scale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #converting to blurred
    blurred_image = cv2.GaussianBlur(gray_scale, (3, 3), 0)
    canny_image = cv2.Canny(gray_scale, 50, 150)
    canny_images = cv2.Canny(blurred_image, 50, 150)
    cv2.imshow("original", image) 
    cv2.imshow("canned", canny_image)
    cv2.imshow("cannwd without blurr", canny_images)
    cv2.waitKey(0)

#edge_detection()
    
def morphical_image():
    """
    Morphological operations involve the manipulation of the
    shape or structure of objects within an image. 
    These operations are useful for tasks like
    noise removal, object detection, and image segmentation.
    """
    image = cv2.imread('images.jpeg')

    gray_scale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Define a structuring element (3x3 kernel)
    kernel = np.ones((3, 3), np.uint8)

# Perform erosion
    eroded_image = cv2.erode(gray_scale, kernel, iterations=1)

# Perform dilation
    dilated_image = cv2.dilate(gray_scale, kernel, iterations=1)
    cv2.imshow('eroded', eroded_image)
    cv2.imshow('dilated', dilated_image)
    cv2.waitKey(0)
morphical_image()