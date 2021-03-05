import cv2 as cv
import numpy as np

# putting the image into a variable
img = cv.imread("fish.jpeg")

# resizing images so they can all fit on my screen
img = cv.resize(img, (250, 250), interpolation= cv.INTER_AREA)
cv.imshow("ORIGINAL",img)

#convert to greyscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("GREY", gray)

#blur an image
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
cv.imshow("BLURRED", blur)

# edge cascade
canny = cv.Canny(img, 125,175)
cv.imshow("EDGES", canny)
# decreasing edges by passing blurred image
canny = cv.Canny(blur, 125,175)
cv.imshow("BLURRED EDGES", canny)

#dilating the image
dilated = cv.dilate(canny, (3,3), iterations = 3)
cv.imshow("DILATED", dilated)

# eroding
eroded = cv.erode(dilated, (3,3), iterations = 3)
cv.imshow("ERODED", eroded)

#cropping
cropped = img[50:200][50:200]
cv.imshow('CROP', cropped)

cv.waitKey(0)
cv.destroyAllWindows()
exit(0)