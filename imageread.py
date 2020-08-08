import cv2

img = cv2.imread("./img.jpg")

cv2.imshow("f",img)
print(img[0])
print(img.shape)
while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()