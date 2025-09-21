import cv2
#for capturing vdo
cap=cv2.VideoCapture(0)
print(cap.isOpened())
# for saving vdo define codec and vdo writter obj
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

while(cap.isOpened()):
    # frame captures the video in color 
    # and ret is boolean var if frame is capturing it returns true
    ret, frame=cap.read()
    if ret :
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        
        out.write(frame)

    #grav convert the frame from color to black and white
        gray= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame',gray)
    
        if cv2.waitKey(1) & 0xFF ==ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()