import cv2
import keyboard as key
import pyautogui
import time
import win32api

def mouse_move(table):
    pyautogui.moveTo(table[0],table[1])
    pyautogui.click(table[0],table[1])

def locate_img(image_files):
    count = 0
    for i in image_files:
        count += 1
        img_loc = pyautogui.locateCenterOnScreen(image_files[count], confidence=0.5)
        if img_loc:
            print('Found Object\n\n\n')
            return img_loc

win32api.MessageBox(None,"Make sure roblox is visible on screen, then press Ok", "Please note", 0)
temp_imgs = ['C:/Users/foxwi/Documents/Lightshot/Screenshot_13.png','C:/Users/foxwi/Documents/Lightshot/Screenshot_12.png']

while True:
    time.sleep(.1)
    Real_img = locate_img(temp_imgs)
    mouse_move(Real_img)
