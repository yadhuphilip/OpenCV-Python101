import cv2

haar = cv2.CascadeClassifier('frontalfacehaar.xml')

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
G = [[1],[123]]
size = 2
while True:
    _,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    rect = haar.detectMultiScale(gray,1.4,3)
     
    for x,y,w,h in rect:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)

    cv2.imshow("sd",frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cv2.destroyAllWindows()