import cv2
img=cv2.imread("C:/Users/SUPRATIM DAS/OneDrive/Pictures/Camera Roll/OneDrive/Desktop/Open-CV/Open-CV-with-Python/Geometry/orange.jpg",1)
print(img)
# (255,0,0) this is BGR format Blue Green Red
img=cv2.line(img, (0,0),(255,255),(255,0,0),5)
img=cv2.rectangle(img,(3,9),(23,44),(0,255,0),8)
img=cv2.circle(img,(447,63),63,(0,0,225), 7)
font=cv2.AGAST_FEATURE_DETECTOR_AGAST_7_12D
img=cv2.putText(img, 'Opencv', (10,500), font,4,(255,255,0),10, cv2.LINE_AA)
cv2.imshow('image2',img)
cv2.waitKey(0) & 0xFF== ord('q')
cv2.destroyAllWindows()