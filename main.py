import cv2
from PIL import ImageGrab
import win32, win32api, win32gui, win32con, win32ui
import numpy as np

class CapWindow:
    def _init_(Name_Of_Window):
        w, h = 1920, 1080

        Window_Name = Name_Of_Window or "Roblox"
        hwnd = win32gui.FindWindow(None, Window_Name)

        wDC = win32gui.GetWindowDC(hwnd)
        dcObj = win32ui.CreateDCFromHandle(wDC)
        cDC = dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, w, h)
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((0, 0), (w, h), dcObj, (0, 0), win32con.SRCCOPY)

        signedIntsArray = dataBitMap.GetBitmapBits(True)
        img = np.fromstring(signedIntsArray, dtype='uint8')
        img.shape = (h, w, 4)

        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(hwnd, wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())

        img = img[...,:3]

        img = np.ascontiguousarray(img)

        return img



def FindTemplates(img, template_img, threshold):

    temp = cv2.imread(template_img)
    img = img
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


while True:
    frame = CapWindow("Roblox")
    temp_img = ""
    FindTemplates(frame,temp_img, 0.4)

    if cv2.waitKey() & 0xff ==ord('q'):
        cv2.destroyAllWindows()
        break