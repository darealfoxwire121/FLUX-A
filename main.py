import cv2
from PIL import ImageGrab
import numpy as np

while True:
    img = np.array(ImageGrab.grab(bbox=(0,0,800,600)))
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    ret, newimg = cv2.threshold(img, 0, 255, cv2.CHAIN_APPROX_NONE)

    cv2.imshow("Tracking",newimg)

    if cv2.waitKey(1) & 0xff ==ord('q'):
        break

cv2.destroyAllWindows()