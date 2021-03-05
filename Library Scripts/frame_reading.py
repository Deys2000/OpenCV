


import cv2

# img = cv2.imread('fish.jpeg', 0)
# print(img)
# cv2.imshow('imagename',img)
# k = cv2.waitKey(0)
# if( k == 27 ):
#     cv2.destroyAllWindows()
# elif k == ord('s'):
#     cv2.imwrite('fish3.png', img)
# cv2.destroyAllWindows()

#  drawing geometric shapes on images
# import numpy as np
# img = np.zeros([512,512,3], np.uint8())
#
# #img = cv2.imread('fish.jpeg', 1)
# # the following line takes pt 1, pt 2, color and thickness
# img = cv2.line(img, (0,0), (255,255), (0,0,255), 5)
# # the following does the same but as an arrow
# img = cv2.arrowedLine(img, (0,255), (255,255), (0,255,0), 5)
# # the following draws a rectangle
# img = cv2.rectangle(img, (384,0), (510, 128), (0,0,255), -1)
# # the following draws a circle
# img = cv2.circle(img, (477, 63), 63, (255, 0,0), -1)
#
# font = cv2.FONT_HERSHEY_SIMPLEX
# img = cv2.putText(img, 'OpenCV', (10,500), font, 4, (255,255,255), 10 , cv2.LINE_AA)
#
# cv2.imshow("image window", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

## ended previous

## Starting from scratch here with freeCodeCamp.org

import cv2 as cv

def changeRes(width, height):
    capture.set(3,width)
    capture.set(4,height)

# img = cv.imread('fish.jpeg')
# cv.imshow('FISH', img)

def rescaleFrame(frame, scale=0.5):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)
    return cv.resize(frame,dimensions,interpolation = cv.INTER_AREA)

#frame_resized2 = rescaleFrame(img)
#cv.imshow('image', frame_resized2)

capture = cv.VideoCapture('Finance Minister Speech.mp4')
# plays the video
while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)
    cv.imshow('Video', frame_resized)
    if(cv.waitKey(20) & 0xFF == ord("d")):
        break

capture.release()
cv.destroyAllWindows()
exit(0)


