import cv2
#read the image
img=cv2.imread('apple.jpg',0)

#give result in a matrix form
print(img)

#show the image as per it reads it
cv2.imshow('image', img)
k=cv2.waitKey(0)
if k==27:
    cv2.destroyAllWindows()
elif k== ord('s'):
    cv2.imwrite('Apple_copy.jpg', img)
    cv2.destroyAllWindows()
