import numpy as np
import cv2
img= cv2.imread('image.png')
img2=cv2.imread('orange.jpg')

print(img.shape) # returns a tuple of no of rows and columns and chanels
print(img.size) #returns totaal no of pixels is accessed
print(img.dtype) #return image datatype
b,g,r=cv2.split(img)
img=cv2.merge((b,g,r))

ball = img[280:340, 330:390]
img[273:333, 100:160]= ball

img=cv2.resize(img, (512,512))
img2=cv2.resize(img2, (512,512))
# dst=cv2.add(img, img2); #merge two images ( to add 2 img we have to make sure those are same size)
dst=cv2.addWeighted(img, .6, img2, .3, 0);
cv2.imshow('image', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()


# ROI= Region of Interest