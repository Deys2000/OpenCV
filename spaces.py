import cv2 as cv
import numpy as np

img = cv.imread("fish.jpeg")
img = cv.resize(img, (img.shape[1]//3, img.shape[0]//3))
cv.imshow("FISH", img)

# BGR to greyscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("GRAY", gray)

# BGR to HSV - hue, saturation, value
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("HSV", hsv)

# BGR to Lab -  dunno what this is
lab = cv.cvtColor(img, cv.COLOR_BGR2Lab)
cv.imshow("LAB", lab)

# BGR to RGB - just inverting the order to red and blue
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("BGR to RGB", rgb)

# of all the conversions above you can also to the inverse of each conversion
# but there are exceptions
# one is that you cannot go from greyscale to HSV for example, so you go grey -> BGR - > HSV
# rule of thumb, just go to BGR and you should be able to convert to whatever

cv.waitKey(0)
cv.destroyAllWindows()
exit(0)
