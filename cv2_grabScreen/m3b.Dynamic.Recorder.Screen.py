import time
import cv2 as cv
import mss
import numpy as np

'''
1. R 作为录像开关（切换器）
2. 屏幕没有变化，则暂停录像，屏幕有变动则录像
'''

TOP = 77; LEFT = 0; WIDTH = 1280; HEIGHT = 720
# TOP = 0; LEFT = 0; WIDTH = 1366; HEIGHT = 768
# TOP = 0; LEFT = 0; WIDTH = 1920; HEIGHT = 1080

monitor = {"top":TOP, "left":LEFT, "width":WIDTH, "height":HEIGHT}
sct = mss.mss()
cv.namedWindow("Video Stream Monitor")

class VideoRecorder(object):
    def __init__(self):
        pass

    def start(self):
        fourcc = cv.VideoWriter_fourcc(*'MP4V') # mp4v-mp4 xvid-mp4 
        gettime = time.strftime("%Y%m%d_%H%M%S")
        self.name = 'RECORD_{}.mp4'.format(gettime)
        # Recorder-1: Define the codec and create VideoWriter object
        self.writer = cv.VideoWriter(self.name, fourcc, 20.0, (WIDTH,  HEIGHT))

    def write(self, img):
        self.writer.write(img)
    
    def release(self):
        self.writer.release()

def textInfo(txt, imgTarget, xpos, ypos):
    ''' Put text infomation on an image '''
    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(imgTarget, txt, (xpos, ypos), font, 0.5, (25,25,25), 5, cv.LINE_AA)
    cv.putText(imgTarget, txt, (xpos, ypos), font, 0.5, (25,255,25), 1, cv.LINE_AA)

def grabScreen():
    ''' The Main Function! '''
    vrecorder = VideoRecorder()

    imgSet = None # x image
    img = None    # y image
    alarm = 0     # 动态定时器
    nonzero = 0
    record_switch = False
    fastMode = False

    btmInfo = "Initializ...."
    btmLife = 4.5  # Bottom Message Life
    tmset = time.time()
    tmnow = time.time()
    interv = tmnow - tmset

    while True:
        imgSet = img  # y --> x
        grabImgTmp = np.array(sct.grab(monitor)) # BGRA 图片
        img = cv.cvtColor(grabImgTmp, cv.COLOR_BGRA2BGR)  # 格式转化
        #img = cv.resize(img, (1280, 720))

        # 动态触发逻辑  nonzero 的数值触发 alarm
        if imgSet is not None:  # x image 获得了图像
            subimg = cv.subtract(img, imgSet)  # 相减
            gray = cv.cvtColor(subimg, cv.COLOR_BGR2GRAY) # 灰度
            _ret, thresh = cv.threshold(gray, 50, 255, cv.THRESH_BINARY) # Threshold
            nonzero = cv.countNonZero(thresh) # 统计非零数值 noZero
            if nonzero > 32:   # 触发定时器
                alarm = 16

        # 定时器逻辑
        alarm -= 1
        if alarm < 0:
            alarm = 0

        # 录像写入条件： 触发状态 (alarm > 0)
        if record_switch and alarm > 0:
            vrecorder.write(img)

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

        textInfo(str(int(interv * 1000)), resizedImg, 20, 106)
        cv.imshow("Video Stream Monitor", resizedImg)
        #cv.moveWindow("Video Stream Monitor", 1350, 750)

        # 按键设置
        if fastMode:
            key = cv.waitKey(300)   # speed Fast! big interv jump.
            nonzero = 0
        else:
            #w = int(33 - interv * 1000)   # speed normal
            #if w <= 0:
                #w = 1
            key = cv.waitKey(35)

        if key == ord('p'): # Recording / Pause Toggle
            record_switch = not record_switch

        elif key == ord('f'): # Fast mode Toggle
            fastMode = not fastMode

        elif key == ord('s'): # Start
            for i in range(3):
                print(3 - i)
                time.sleep(1)
            print("Recording start!")
            vrecorder.start()
            record_switch = True
            btmLife = 4.5
            btmInfo = "Start Recording!"
            print("===> Start Recording!")

        elif key == ord('x'): # Stop
            record_switch = False
            vrecorder.release()
            btmLife = 4.5
            btmInfo = "Recording Stopped, video file saved!"
            print("===> saved...\n")

        elif key & 0xff == 27:
            break

        # bottom information
        tmset = tmnow
        tmnow = time.time()
        interv = tmnow - tmset
        xfps = int(1.0 / interv)

        btmLife -= interv
        if btmLife < 0:
            btmLife = 0
        else:
            textInfo(btmInfo, resizedImg, 20, 250)
        
    #  关闭所有窗口
    cv.destroyAllWindows()

if __name__ == "__main__":
    grabScreen()
    print("Done!")
