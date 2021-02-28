import cv2
from PIL import ImageGrab
import numpy as np


def FindTemplates(template_img, threshold):

    temp = cv2.imread(template_img)
    img = np.array(ImageGrab.grab())
    result = cv2.matchTemplate(img, temp, cv2.TM_CCOEFF_NORMED)

    locations = np.where(result >= threshold)
    locations = list(zip(*locations[::-1]))

    if locations:
        print('Found template')
        for loc in locations:

            width = temp.shape[1]
            height = temp.shape[0]

            if loc[0] and loc[1]:
                top_left = loc
                bottom_right = (top_left[0] + width, top_left[1] + height)

                cv2.rectangle(img, top_left, bottom_right, (0,255,0), 1, 4)

        cv2.imshow('Tacking',img)
        cv2.waitKey()

    else:
        print("Could not find template")


FindTemplates("TEMPLATE MATCH IMAGE DIRECTORY HERE", 0.4)