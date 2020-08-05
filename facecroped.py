import cv2



cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
haar = cv2.CascadeClassifier("frontalfacehaar.xml")
while True:

    ret,frame = cap.read()

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    rects = haar.detectMultiScale(gray,1.2,3)

    for x,y,w,h in rects:
        face = frame[y:y+h,x:x+w]

    cv2.imshow("As",face)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    

cv2.destroyAllWindows()
