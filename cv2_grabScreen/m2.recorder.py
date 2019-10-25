import time
import cv2 as cv
import mss
import numpy as np
from PIL import ImageGrab
import sys

put = sys.stdout.write

title = "Grab Screen"
monitor = {"top":40, "left":0, "width":640, "height":480}
sct = mss.mss()

cv.namedWindow(title)

# Recorder-1: Define the codec and create VideoWriter object
filename = time.strftime("%Y")
fourcc = cv.VideoWriter_fourcc(*'MP4V')
out = cv.VideoWriter('res.mp4', fourcc, 20.0, (640,  480))

def textInfo(txt, imgTarget, xpos, ypos):
    ''' Put text infomation on an image '''
    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(imgTarget, txt, (xpos, ypos), font, 0.5, (25,25,25), 5, cv.LINE_AA)
    cv.putText(imgTarget, txt, (xpos, ypos), font, 0.5, (25,255,25), 1, cv.LINE_AA)

def grabScreen():

    imgSet = None
    im = None

    time_set = time.time() # for FPS logic
    FPS = 0
    count = 0

    while True:
        imgSet = im
        im = np.array(sct.grab(monitor)) # BGRA

        im = np.flip(im[:, :, :3], 2)  # 1
        img = cv.cvtColor(im, cv.COLOR_BGR2RGB)  # 2

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

        # write the frame
        out.write(img)
        cv.imshow('frame', img)

        key = cv.waitKey(25)
        if key & 0xff == 27:
            break
        
    out.release()
    cv.destroyAllWindows()

#screen_recordPIL()
grabScreen()
print("Done!")

#1 https://www.therightchoyce.com/2018/10/01/setting-up-visual-studio-code-with-pipenv-and-python3/
#2   Setting up Visual Studio Code with pipenv and python3


'''
Redefine MSSSource.frame() to:

def frame(self):
    monitor = {'top': 0, 'left': 0, 'width': 640, 'height': 480}
    im = numpy.array(self.sct.grab(monitor))
    im = numpy.flip(im[:, :, :3], 2)  # 1
    im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)  # 2
    return True, im
MSS returns raw pixels in the BGRA form (Blue, Green, Red, Alpha). So #1 will reshape from BGRA to BGR and #2 will convert BGR to RGB.
'''