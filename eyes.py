import cv2

eyes = cv2.CascadeClassifier("eyes.xml")
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
while True:

    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    rects = eyes.detectMultiScale(gray,1.1,2)

    for x,y,w,h in rects:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),1)
    cv2.imshow("frame",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()