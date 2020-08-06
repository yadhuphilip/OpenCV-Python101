import cv2

hand = cv2.CascadeClassifier("hand.xml")

cap = cv2.VideoCapture(0)

while True:

    _, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    rects = hand.detectMultiScale(gray,1.1,4)

    for x,y,w,h in rects:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),1)
    
    cv2.imshow("fra", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    

cap.release()
cv2.destroyAllWindows()