#To do:
# add roblox height and width as bbox
# make it loop, and take screenshots
# give keyboard output depending on location of lines

import cv2 as cv
import matplotlib.pylab as plt
import numpy as np

img = cv.imread(r"C:\Users\foxwi\Documents\Lightshot\Screenshot_19.png")
ret, newImg = cv.threshold(img, 230, 255, cv.THRESH_BINARY, None)

#dark image with nothing
darkImg = np.zeros(img.shape[:2], dtype='uint8')

#draw ROI on dark image
pts = np.array([[51,299], [243,192], [329,192], [513,299]], np.int32)
pts = pts.reshape((-1,1,2))

#poly shaped image
poly = cv.fillPoly(darkImg.copy(), [pts], (255,0,0), None, None)

#real img with poly shape overlay
polyimg = cv.fillPoly(img.copy(), [pts], (255,0,0), None, None)

#create masked image with ROI
new_shape = cv.bitwise_and(img,img, mask=poly)

#create ROI threshold
ret, threshmask = cv.threshold(new_shape, 120, 255, cv.THRESH_BINARY, None)

#grab egdes and lines
egdes = cv.Canny(threshmask, 50, 100, None, None, None)
lines = cv.HoughLinesP(egdes, 1, np.pi/180, 30, None, None, 200)

#draw actual lines on all lines
newNum = 0
while newNum < len(lines):
    for x1,y1,x2,y2 in lines[newNum]:
        cv.line(img,(x1,y1), (x2,y2), (0,255,0), 3, None, None)
    newNum += 1

plt.imshow(img)
#plt.show()
cv.imshow("Poly Shape",poly)
cv.imshow("Image with lines", img)
cv.imshow("Threshold Image", newImg)
cv.imshow("Modified Image", new_shape)
cv.imshow("Real image + Poly overlay",polyimg)
cv.imshow("Threshold for masked image", threshmask)
cv.waitKey(0)
cv.destroyAllWindows()