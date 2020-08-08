import cv2

img = cv2.imread("./img.jpg")
ls = []
#remove blue channel
GR = img.copy()
GR[:,:,0] = 0
ls.append(GR)

BR = img.copy()
BR[:,:,1] = 0


BG = img.copy()
BG[:,:,2] = 0
ls.append(BG)
ls.append(BR)
for each in range(len(ls)):
    cv2.imshow("f{}".format(str(each)),ls[each])

while True:
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

