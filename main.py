import cv2

img = cv2.imread('fish.jpeg', 0)

#print(img)

cv2.imshow('imagename',img)
k = cv2.waitKey(0)

if( k == 27 ):
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('fish3.png', img)
cv2.destroyAllWindows()

