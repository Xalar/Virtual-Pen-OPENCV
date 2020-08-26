import cv2
import numpy as np

framewidth = 640
frameheight = 480

cap = cv2.VideoCapture(0)
cap.set(3, framewidth)
cap.set(4, frameheight)
cap.set(10, 130)

mycolors = [[5,107, 0, 19, 255, 255],
            [133, 56, 159, 156, 255],
            [57, 76, 0, 100, 255, 255]]

def findcolor(img, mycolors):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    for color in mycolors:
        lower = np.array(mycolors[0][0:3])
        upper = np.array(mycolors[0][3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        cv2.imshow(str(color[0]), mask)

while True:
    success, img = cap.read()
    findcolor(img, mycolors)
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
