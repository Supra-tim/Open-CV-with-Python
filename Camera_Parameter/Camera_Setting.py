import cv2
cap=cv2.VideoCapture(0)
print(cap.isOpened())
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# 3 is the associative no of Height and 4 for Width
cap.set(3, 3000)
cap.set(4, 700)
print(cap.get(3))
print(cap.get(4))

while(cap.isOpened()):
    ret,frame=cap.read()
    if ret == True:
        gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
cap.destroyAllWindows()
