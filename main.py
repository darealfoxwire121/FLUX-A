import cv2
import keyboard as key
import pyautogui
import time
import win32api


#Move mouse to x and y coordinates
def mouse_move(x , y):

    #windows api's movement is faster than other modules
    win32api.mouse_event( "MOUSEEVENTF_ABSOLUTE" , x , y , 0 , None )


#Get the center coordinates of the image
def center_img(image_parts):

    #Top + Height //2 ; Left + Width//2
    return ( ( image_parts.Image_Top + image_parts.Image_Height//2 ) , ( image_parts.Image_left + Image_width//2 ) )


#locate image on screen
def locate_img(image_file):

    #Use OpenCV to locate the template image on screen using confidence, the higher, the more strict
    img_loc = pyautogui.locateOnScreen( image_file , confidence=0.5 )

    #if location exists
    if img_loc != None:

        #all the parts of the image needed
        Image_Parts = {
            "Image_Top": img_loc[0],
            "Image_left": img_loc[1],
            "Image_width": img_loc[2],
            "Image_Height": img_loc[3],
        }

        return Image_Parts


#Make sure roblox is in view
win32api.MessageBox(None,"Make sure roblox is visible on screen, then press Ok", "Please note", 0)


#Grab the temp_img file to be used for searching
temp_img = 'C:/Users/foxwi/Documents/Lightshot/Screenshot_12.png'


#Looks for objects every time the loop runs, stops when ctrl+c
while True:
    
    #delay
    time.sleep(.5)

    #Grab the center to the found image
    Real_img = center_img(locate_img(temp_img))

    #Move mouse to the Real_img's center ( In this case, should be the enemy's head )
    mouse_move( Real_img[0] , Real_img[1] )
