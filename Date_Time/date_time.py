import cv2
import datetime
cap=cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
cap.set(3, 620)
cap.set(4, 720)
print(cap.get(3))
print(cap.get(4))
while(cap.isOpened()):
    ret,frame=cap.read()
    if ret== True:
        #gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        font=cv2.FONT_HERSHEY_SIMPLEX
        text=' Width: '+ str(cap.get(3)) + 'Height: ' + str(cap.get(4))
        datet=str(datetime.datetime.now())
        frame=cv2.putText(frame, datet, (20,30),font,1,(0,255,255),2,cv2.LINE_AA)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.relese()
cap.destroyAllWindows()
