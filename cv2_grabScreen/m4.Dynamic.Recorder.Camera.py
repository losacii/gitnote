import time
import cv2 as cv
import mss
import numpy as np
from PIL import ImageGrab
import sys

'''
1. R 作为录像开关（切换器）
2. 视频流没有变化，则暂停录像，屏幕有变动则录像
'''

put = sys.stdout.write

cv.namedWindow("Video Stream Monitor")

cap = cv.VideoCapture(0)

# Recorder-1: Define the codec and create VideoWriter object
WIDTH,  HEIGHT = 640, 480
gettime = time.strftime("%Y%m%d_%H%M%S")
fourcc = cv.VideoWriter_fourcc(*'MP4V')
videoWriter = cv.VideoWriter('screen_recording_{}.mp4'.format(gettime), fourcc, 20.0, (WIDTH,  HEIGHT))

def textInfo(txt, imgTarget, xpos, ypos):
    ''' Put text infomation on an image '''
    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(imgTarget, txt, (xpos, ypos), font, 0.5, (25,25,25), 5, cv.LINE_AA)
    cv.putText(imgTarget, txt, (xpos, ypos), font, 0.5, (25,255,25), 1, cv.LINE_AA)

def grabScreen():
    ''' The Main Function! '''

    imgSet = None # x image
    img = None    # y image
    alarm = 0     # 动态定时器
    record_switch = False

    while True:
        imgSet = img  # y --> x
        _ret, img = cap.read()

        if imgSet is not None:  # x image 获得了图像
            subimg = cv.subtract(img, imgSet)  # 相减
            gray = cv.cvtColor(subimg, cv.COLOR_BGR2GRAY) # 灰度
            _ret, thresh = cv.threshold(gray, 127, 255, cv.THRESH_BINARY) # Threshold
            nonzero = cv.countNonZero(thresh) # 统计非零数值 noZero
            if nonzero > 0:   # 触发定时器
                alarm = 90

        # 定时器逻辑
        alarm -= 1
        if alarm < 0:
            alarm = 0

        # 录像写入条件： 触发状态 (alarm > 0)
        if record_switch and alarm > 0:
            cpimg = img.copy()
            tm = time.strftime("%Y-%m-%d %H:%M:%S")
            textInfo(tm, cpimg, 30, 30)
            videoWriter.write(cpimg)

        # 显示缩小图和信息
        showImg = img.copy()
        resizedImg = cv.resize(showImg, (320, 240))
        textInfo("Alarm Level: {}, Recording: {}".format(alarm, record_switch), resizedImg, 10, 20)
        cv.imshow("Video Stream Monitor", resizedImg)
        #cv.moveWindow("Video Stream Monitor", 1350, 750)

        # 按键设置
        key = cv.waitKey(45)
        if key == ord('r'):
            record_switch = not record_switch
        elif key & 0xff == 27:
            break
        
    # 结束， 释放录像, 关闭所有窗口
    videoWriter.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    grabScreen()
    print("Done!")