import cv2
import numpy as np
import keyboard
import pyautogui
import os
import subprocess
import time

import win32api
import math

realimg = None
x = 0

temp_file_loc = ""

win32api.MessageBox(None,"Open roblox then press ok", "notice", 0)
temp_img = cv2.cvtColor(temp_file_loc,cv2.COLOR_RGB2GRAY)
pyautogui.screenshot('Newimage.png')

for pnts in pyautogui.locateAllOnScreen(temp_img, confidence=0.4):
    realimg = cv2.imread('Newimage.png', cv2.TM_CCOEFF)
    realimg = cv2.cvtColor(realimg, cv2.COLOR_RGB2GRAY)
    pnts_left = pnts[0]
    pnts_top = pnts[1]
    pnts_width = pnts[2]
    pnts_height = pnts[3]
    x += 1
    print("Found "+str(x))
    cv2.rectangle(realimg, ((pnts_left),(pnts_top - pnts_height + (pnts_height//2))), ((pnts_left + pnts_width),(pnts_top + pnts_height)), (0,255,255), 2)
    if x > 100:
        break

cv2.imshow('Detected',realimg)
cv2.waitKey()
cv2.destroyAllWindows()
    
