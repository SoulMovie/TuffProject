import cv2
import time

edit = cv2.VideoCapture(0)Q
i = 90
while True:
    ret, frame = edit.read()
    frame = cv2.flip(frame, 1)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = cv2.blur(frame, (5, 5))
    frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
    cv2.imshow('Edit', frame)
    i += 90

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cv2.destroyAllWindows()