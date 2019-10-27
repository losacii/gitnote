# import packages
from PIL import Image
from subprocess import Popen, PIPE
from imutils.video import VideoStream
from imutils.object_detection import non_max_suppression
from imutils import paths
import cv2
import numpy as np
import imutils

# ffmpeg setup
p = Popen(['ffmpeg', '-y', '-f', 'image2pipe', '-vcodec', 'mjpeg', '-r', '24', '-i', '-', '-vcodec', 'h264', '-qscale', '5', '-r', '24', 'video.mp4'], stdin=PIPE)

video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    if ret:
        frame.save(p.stdin, 'JPEG')
    else:
        break

p.stdin.close()
p.wait()
video.release()
cv2.destroyAllWindows()