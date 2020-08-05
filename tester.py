import cv2


import numpy as np

cap = cv2.VideoCapture(0)

a,b = cap.read()
c = cv2.rect(100,100,200,300)
cv2.imshow("frame1",b)
#cv2.imshow("frame2",c)
cv2.waitKey(0)

#print(type(b),type(c),b[80],c[80],c.shape)

        #(x, y, w, h) = [v * size for v in f] #Scale the shapesize backup
        x,y,w,h = f
        #cv2.rectangle(frame, (x, y), (x + w, y + h),(0,255,0),thickness=4)
        #Save just the rectangle faces in SubRecFaces
        sub_face = frame[y:y+h, x:x+w]

    # Show the image
    cv2.imshow('asd', sub_face)

    if cv2.waitKey(1) & 0xFF == ord('q'):