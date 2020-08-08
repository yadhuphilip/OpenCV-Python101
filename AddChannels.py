import cv2
import numpy as np
img = (250,200,3)
Channels = np.zeros(img,dtype = np.uint8)
print(Channels.shape,type(Channels[0][0][0]))

Blue = Channels.copy()
Blue[:,:,0] = 254

Green = Channels.copy()
Green[:,:,1] = 254

Red = Channels.copy()
Red[:,:,2] = 254

White = Red.copy()
White[:,:,0] = 254
White[:,:,1] = 254


ls = [Red,Blue,Green,White,Channels]

for i in range(len(ls)):
    cv2.imshow("fd {}".format(i),ls[i])

while True:

    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break

cv2.destroyAllWindows()