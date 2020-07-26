import cv2 # importing opencv library

imgOriginalCol = cv2.imread('text.jpeg', 1) # reading original size image in coloured format

#GRAY SCALE CONVERSION
imgGray = cv2.cvtColor(imgOriginalCol, cv2.COLOR_RGB2GRAY) # converting image color to gray
cv2.imshow("Gray scale image ", imgGray)  # here image object is imgGray
#HSV CONVERSION
imgHsv = cv2.cvtColor(imgOriginalCol, cv2.COLOR_RGB2HSV)  # converting image color to HSV
cv2.imshow("HSV image", imgHsv) # here image object is imgHsv
#RESIZING ORIGINAL IMAGE
imgResize = cv2.resize(imgOriginalCol, (300, 300)) # providing resizing dimensions
cv2.imshow('Resized original image', imgResize) # displaying resized image
#SHAPE VALUES
print("Original colored image - Shape : ", imgOriginalCol.shape) # output has three values (height, width, channel)
print("Resize colored image - Shape : ", imgResize.shape) # output has three values (height, width, channel)
#SIZE VALUES
print("Original colored image - Size : ", imgOriginalCol.size) # printing original colored image size
print("Resize colored image - Size : ", imgResize.size) # printing resize colored image size
#THRESHOLDING OPERATIONS
ret, thresh = cv2.threshold(imgGray, 150, 255, cv2.THRESH_BINARY)
ret, thresh1 = cv2.threshold(imgGray, 150, 255, cv2.THRESH_BINARY_INV)
ret, thresh2 = cv2.threshold(imgGray, 150, 255, cv2.THRESH_OTSU)
adaptive_thresh = cv2.adaptiveThreshold(imgGray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 1.5)
adaptive_thresh1 = cv2.adaptiveThreshold(imgGray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, 1.5)
# display output
cv2.imshow('threshold binary', thresh)
cv2.imshow('threshold binary inversion', thresh1)
cv2.imshow('threshold otsu', thresh2)
cv2.imshow('threshold adaptive', adaptive_thresh)
cv2.imshow('threshold adaptive gaussian', adaptive_thresh)

#SAVING IMAGES
cv2.imwrite("gray_scale_conversion.jpg", imgGray)
cv2.imwrite("hsv_conversion.jpg", imgHsv)
cv2.imwrite("thresh_binary.jpg", thresh)
cv2.imwrite("thresh_binary_inv.jpg", thresh1)
cv2.imwrite("thresh_otsu.jpg", thresh2)
cv2.imwrite("adaptive_thresh_mean.jpg", adaptive_thresh)
cv2.imwrite("adaptive_thresh_gaussian.jpg", adaptive_thresh1)

#EXIT CONTROL
cv2.waitKey(0)
cv2.destroyAllWindows()