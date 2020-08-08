import cv2
import numpy as np


cap = cv2.VideoCapture(0)

while True:
    _,img = cap.read()
    img = cv2.flip(img,1)

    for i in range(3):
        C = np.zeros(img.shape,dtype = np.uint8)
        C[:,:,i] = img[:,:,i]
        cv2.imshow("frame {}".format(str(i)),C)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
    