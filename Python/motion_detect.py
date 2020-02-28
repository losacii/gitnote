# coding:utf-8
import cv2
import numpy as np
import time, datetime, os
from numpy import log

camIndex = 0
frameList = []

cap = cv2.VideoCapture(camIndex)
fps = 20

winName = "Camera_" + str(camIndex)

cv2.namedWindow(winName, cv2.WINDOW_AUTOSIZE)

# time mapping
motionData = [0]
mtPast = time.time()
secondsCount = 0
motionIndex = 0

# ! On Linux
# writer = cv2.VideoWriter('/home/losacii/Pictures/cv/cap' + time.strftime("%Y-%m-%d_%H%M%S") + '.avi', cv2.cv.CV_FOURCC(*'DIVX'), 33, (640,480))


def checkMotion(xframe, yframe):
    diff = cv2.absdiff(xframe, yframe)
    _, thresh = cv2.threshold(diff, 12, 255, cv2.THRESH_BINARY)
    kernel = np.ones((2, 2), np.uint8)
    erosion = cv2.erode(thresh, kernel, iterations=1)

    x = cv2.countNonZero(erosion)
    if x > 16:
        return [True, x]
    return [False, 0]


recordingTimeRemain = 0
recordFrame = None


def recordingTimeReset():
    global recordingTimeRemain
    recordingTimeRemain = 2


def recordFrame(frame):
    global vfile, videoName
    #vfile.write(frame)


def sendFrame(frame, ip, port):
    pass


def run():
    global recordingTimeRemain, recordFrame, vfile, mtPast, secondsCount, motionIndex

    pastFrame = cv2.cvtColor(cap.read()[1], cv2.COLOR_RGB2GRAY)
    print(pastFrame.shape)
    pastTime = time.time()
    running = True

    #fourcc = cv2.VideoWriter_fourcc(*'MP4V')
    #vfileName = 'vcap_' + time.strftime("%Y-%m-%d-%H%M%S") + '.mp4'
    #vfile = cv2.VideoWriter(vfileName, fourcc, fps, (640, 480))

    font = cv2.FONT_HERSHEY_SIMPLEX

    while running:
        _, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

        now = time.time()
        if now - mtPast > 1.0:

            secondsCount += 1
            if motionIndex > 0 and secondsCount > 300:
                motionIndex = 0

                # save file
                pass

            mtPast = now
            motionData.append(0)

        interval = now - pastTime
        pastTime = now

        moving, motionIndex = checkMotion(gray, pastFrame)
        motionData[-1] += int(log(motionIndex + 1))

        if moving:
            recordingTimeReset()

        # text info
        showTime = time.strftime("%Y-%m-%d_%H:%M:%S")
        secDigits = datetime.datetime.now().microsecond.__str__()[:2]
        info = "{0}{1}.{2}".format('REC_', showTime, secDigits)
        cv2.putText(frame, info, (35, 25), font, 0.5, (20, 20, 20), 3)
        cv2.putText(frame, info, (35, 25), font, 0.5, (0, 255, 0), 1)

        # check to see if it's time to record frame
        if recordingTimeRemain > 0:

            # circle
            center = (20, 20)
            radius = 6
            color = (50, 50, 50)
            lineWidth = -1
            cv2.circle(frame, center, radius, color, lineWidth)
            radius = 5
            color = (50, 50, 255)
            cv2.circle(frame, center, radius, color, lineWidth)

            # line
            lineLen = int(recordingTimeRemain * 300)
            y = 10
            start = (20, y)
            end = (20 + lineLen, y)
            lineColor = (200, 200, 0)
            cv2.line(frame, start, end, lineColor, 2)

            # --- recording frame here ---
            recordingTimeRemain -= interval
            # recordFrame(frame)                                         # SWITCH : RECORD

        pastFrame = gray

        # video show
        cv2.imshow(winName, frame)  # SWITCH : SHOW VIDEO

        # keyboard processing
        key = cv2.waitKey(1000 // fps) & 0xff

        if key == 27:  # stop running
            running = False

    cap.release()
    # vfile.release()
    cv2.destroyAllWindows()

    import matplotlib.pyplot as plt
    plt.plot(motionData)
    plt.show()


if __name__ == '__main__':

    run()
