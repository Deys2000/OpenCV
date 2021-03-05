import cv2 as cv
import numpy as np

#getting the image and resizing it
img = cv.imread("fish.jpeg")
img = cv.resize(img, (img.shape[1]//2, img.shape[0]//2))
cv.imshow("FISH", img)

# making a blank image of the same size
blank = np.zeros(img.shape, dtype = 'uint8')
cv.imshow("BLANK", blank)

# making a greyscale image
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("GRAY", gray)

#blurring it before making contours
blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow("BLURRED", blur)

# making canny edges
thresholdOne = 125; thresholdTwo = 175
canny = cv.Canny(img, thresholdOne, thresholdTwo)
cv.imshow("CANNY EDGES", canny)

# thresholding- binarizing the image (into just two colors)
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow("THRESH", thresh)

# RETR_LIST returns all the contours in the image
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found')

cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow("Drawn Contours", blank)

cv.waitKey(0)
cv.destroyAllWindows()
exit(0)