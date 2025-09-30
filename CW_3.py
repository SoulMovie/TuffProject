import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
img[:] = 214, 193, 88

cv2.rectangle(img, (100, 100), (256, 256), (255, 255, 255), cv2.FILLED)
cv2.rectangle(img, (500, 100), (356, 256), (255, 255, 255), cv2.FILLED)

cv2.rectangle(img, (150, 150), (256, 256), (0, 0, 0), cv2.FILLED)
cv2.rectangle(img, (450, 150), (356, 256), (0, 0, 0), cv2.FILLED)

cv2.line(img, (150, 350), (450, 450), (0, 0, 0))
cv2.line(img, (150, 450), (450, 350), (0, 0, 0))

cv2.putText(img, "Kaska glisst", (256, 400), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, (255, 255, 255))


cv2.imshow("Original", img)

cv2.waitKey(0)
cv2.destroyAllWindows()