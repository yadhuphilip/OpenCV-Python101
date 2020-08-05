import cv2
import numpy as np

    # Read image

cap = cv2.VideoCapture(0)
while True:
    ret,im = cap.read()
    x,y,_ = im.shape
    newim = im[x//2:]
    # Select ROI
  
    # Crop image
    cv2.imshow("f1",im)
    cv2.imshow("f2",newim)
    # Display cropped image
    #cv2.imshow("Image", im)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()