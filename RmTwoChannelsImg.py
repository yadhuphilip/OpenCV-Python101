import cv2
import numpy as np


img = cv2.imread("./img.jpg")


for i in range(3):
    C = np.zeros(img.shape,dtype = np.uint8)
    C[:,:,i] = img[:,:,i]
    cv2.imshow("frame {}".format(str(i)),C)
while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
    