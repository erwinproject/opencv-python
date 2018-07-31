import cv2
import numpy as np

videoCam = cv2.VideoCapture(1)

while True:
    cond, frame = videoCam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 100)

    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        for (x,y,radius) in circles:
            cv2.circle(frame, (x,y),radius, (0,255,0), 4)
            #cv2.rectangle(frame, (x - 5, y - 5), (x + 5, y + 5), (0,128,255),1)
            nilaix = str(x)
            nilaiy = str(y)
            nilair = str(radius)
            if radius > 10:
                print('nilai x = ' + nilaix + ' | nilai y = ' + nilaiy + ' | nilai radius = ' + nilair)

    
    cv2.imshow('Original Video', frame)
    
    
    #cv2.imshow('Gray Video', gray)

    k = cv2.waitKey(1) & 0xff
    if k == ord('q'):
        break

videoCam.release()
cv2.destroyAllWindows()
