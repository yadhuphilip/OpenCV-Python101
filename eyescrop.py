import cv2

eyes = cv2.CascadeClassifier("eyes.xml")

cap = cv2.VideoCapture(0)

while True:

    _,frame = cap.read()

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
   

    rect = eyes.detectMultiScale(gray,1.1,2)
    print("sas")
    ls = []
    subimg = frame[100:250,100:250]
    ls.append(subimg)
    for x,y,w,h in rect:

        subimg = frame[y:y+h,x:x+w]
        ls.append(subimg)
    for i in range(len(ls)):
        f = "c" + str(i)
        cv2.imshow(f, ls[i])

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()