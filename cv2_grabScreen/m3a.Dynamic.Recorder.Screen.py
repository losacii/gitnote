import time
import cv2 as cv
import mss
import numpy as np
from PIL import ImageGrab
import sys

'''
1. R 作为录像开关（切换器）
2. 屏幕没有变化，则暂停录像，屏幕有变动则录像
'''

put = sys.stdout.write

WIDTH = 1280; HEIGHT = 720
monitor = {"top":45, "left":0, "width":WIDTH, "height":HEIGHT}
sct = mss.mss()
cv.namedWindow("Video Stream Monitor")

# Recorder-1: Define the codec and create VideoWriter object
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
    nonzero = 0
    record_switch = False

    fastMode = False

    while True:
        imgSet = img  # y --> x
        im = np.array(sct.grab(monitor)) # BGRA 图片
        img = cv.cvtColor(im, cv.COLOR_BGRA2BGR)  # 格式转化

        if imgSet is not None:  # x image 获得了图像
            subimg = cv.subtract(img, imgSet)  # 相减
            gray = cv.cvtColor(subimg, cv.COLOR_BGR2GRAY) # 灰度
            _ret, thresh = cv.threshold(gray, 50, 255, cv.THRESH_BINARY) # Threshold
            nonzero = cv.countNonZero(thresh) # 统计非零数值 noZero
            if nonzero > 32:   # 触发定时器
                alarm = 18

        # 定时器逻辑
        alarm -= 1
        if alarm < 0:
            alarm = 0

        # 录像写入条件： 触发状态 (alarm > 0)
        if record_switch and alarm > 0:
            videoWriter.write(img)

        # 显示缩小图和信息
        showImg = img.copy()
        resizedImg = cv.resize(showImg, (480, 270))
        textInfo("FastMode: {}, Recording: {}".format(fastMode, record_switch), resizedImg, 10, 20)
        textInfo("Alarm Level: {}".format(alarm), resizedImg, 10, 40)
        textInfo("NonZero: {}".format(nonzero), resizedImg, 10, 60)
        if record_switch:
            if alarm > 0:  # RED sign
                cv.circle(resizedImg,(20,80), 12, (0,0,255), -1)
            else:          # Yellow sign
                cv.circle(resizedImg,(20, 80), 12, (0,255,255), -1)
            if fastMode:
                textInfo("F".format(nonzero, alarm), resizedImg, 16, 86)
        cv.imshow("Video Stream Monitor", resizedImg)
        #cv.moveWindow("Video Stream Monitor", 1350, 750)

        # 按键设置
        if fastMode:
            key = cv.waitKey(300)
            nonzero = 0
        else:
            key = cv.waitKey(29)
        if key == ord('r'):
            record_switch = not record_switch
        elif key == ord('f'):
            fastMode = not fastMode
        elif key & 0xff == 27:
            break
        
    # 结束， 释放录像, 关闭所有窗口
    videoWriter.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    grabScreen()
    print("Done!")