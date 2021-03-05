import cv2 as cv
import numpy as np

#create a blank image
blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow("BLANK", blank)

# Paint the image a certain color
blank[200:300, 300:400] = 0,255,0
cv.imshow('Green', blank)

#drawing a rectangle
cv.rectangle(blank,(0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness = -20)
cv.imshow("rectangle", blank)

#drawing circles
cv.circle(blank, (blank.shape[1]//2,blank.shape[0]//2), 200, (255,0,0), 2)
cv.imshow("CIRCLE", blank)

# drawing lines
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,0,255), 5)
cv.imshow("LINE", blank)

#writing text
cv.putText(blank, "Lorem Ipsum", (225, 225), cv.FONT_HERSHEY_TRIPLEX, 1, (255,255,255), 1 )
cv.imshow("TEXT", blank)

cv.waitKey(0)
cv.destroyAllWindows()
exit(0)
