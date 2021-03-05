import cv2 as cv
import numpy as np

img = cv.imread("fish.jpeg")
cv.imshow("FISH", img)

# Translation
def translate( img, x, y):
    # create a translation matrix, which takes in two lists
    transMat = np.float32([[1,0,x],[0,1,y]])
    # get the dimensions of the image, width and height
    dimensions = (img.shape[1], img.shape[0])
    # this takes the image, a matrix that determines the translation and the dimensions of the original image
    return cv.warpAffine(img, transMat, dimensions)

# The following shows which direction a number causes a translation
# -x -> Left
# -y -> Up
# x -> Right
# y -> Down

translated = translate(img, img.shape[1]//3, img.shape[0]//3)
cv.imshow("Translated", translated)

# Rotation
def rotate(img, angle, rotPoint = None):
    (height, width) = img.shape[:2]
    if( rotPoint == None):
        rotPoint = (width//2,height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 45)
rotated = rotate(rotated, -45)
cv.imshow("ROTATED", rotated)

# Resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow("RESIZED", resized)

# Flipping - parameters 0,1 and -1
flip = cv.flip(img, 0)
cv.imshow("FLIPPED BOTH", flip)

# Cropping
cropped = img[200:400, 300:400]
cv.imshow("CROPPED", cropped)

cv.waitKey(0)
cv.destroyAllWindows()
exit(0)
