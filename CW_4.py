import cv2
import numpy as np

img = cv2.imread("image/hogridar.jpg")

img_copy = img.copy()

img_copy = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)
img_copy = cv2.blur(img_copy, (7, 7))
img_copy = cv2.equalizeHist(img_copy)
img_copy = cv2.Canny(img_copy, 100, 150)

contours, hierarchy = cv2.findContours(img_copy, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    area = cv2.contourArea(cnt)
    if area > 150 and area < 500:
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.drawContours(img, [cnt], -1, (3, 186, 252), 2)
        cv2.rectangle(img, (x, y), (x + w, y + h), (199, 199, 103), 2)
        text_y = y -5 if y - 5 > 10 else y + 15
        text = f'x:{x}, y: {y}, S:{int(area)}'
        cv2.putText(img, text, (x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255))



cv2.imshow("Original", img)
cv2.imshow("Gray", img_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()