# this script is a tutorial on how to split and merge color channels
import cv2 as cv
import numpy as np

img = cv.imread('Fish.jpeg')
img = cv.resize(img, (img.shape[1]//3, img.shape[0]//3))
cv.imshow("FISH", img)

blank = np.zeros(img.shape[:2], dtype='uint8')

# split() basically splits an image into three color matrices, blue green and red
b,g,r = cv.split(img)

blue = cv.merge([b,blank, blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank, blank, r])

cv.imshow('BLUE' , blue)
cv.imshow('GREEN', green)
cv.imshow('RED'  , red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge((b,g,r))
cv.imshow("MERGED", merged)

cv.waitKey(0)
cv.destroyAllWindows()
exit(0)
