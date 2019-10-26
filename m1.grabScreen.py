
import time
import cv2 as cv
import mss
import numpy as np
from PIL import ImageGrab
import sys

put = sys.stdout.write

#mon = (0, 40, 800, 640)
#fps = 0
#display_time = 2

title = "Grab Screen"
monitor = {"top":40, "left":0, "width":960, "height":540}
sct = mss.mss()

cv.namedWindow(title)

def textInfo(txt, imgTarget, xpos, ypos):
    ''' Put text infomation on an image '''
    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(imgTarget, txt, (xpos, ypos), font, 0.5, (25,25,25), 5, cv.LINE_AA)
    cv.putText(imgTarget, txt, (xpos, ypos), font, 0.5, (25,255,25), 1, cv.LINE_AA)

def grabScreen():

    time_set = time.time() # for FPS logic
    FPS = 0
    count = 0

    while True:
        img = np.asarray(sct.grab(monitor)) # this is Fast!

        # FPS logic
        count += 1
        if count >= 32:
            count = 0

            now = time.time()
            interv = now - time_set
            FPS = int(32.0 / interv)
            time_set = now

        # Informations (text and shaps on window)
        cv.rectangle(img, (30, 30, int(FPS) * 6, 30), (20, 255, 20), -1)
        textInfo("Grab Screen FPS: {}".format(str(FPS)), img, 40, 50)

        cv.imshow(title, img)

        key = cv.waitKey(1)
        if key & 0xff == 27:
            break

#screen_recordPIL()
grabScreen()
print("Done!")

#1 https://www.therightchoyce.com/2018/10/01/setting-up-visual-studio-code-with-pipenv-and-python3/
#2   Setting up Visual Studio Code with pipenv and python3