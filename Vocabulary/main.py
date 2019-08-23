# coding:utf-8
import os, sys
import time
import random
import re

#import threading
#import pygame
#
#def playStrokeSound():
#    pygame.mixer.music.play()
#    while pygame.mixer.music.get_busy(): 
#        pygame.time.Clock().tick(10)

rows, columns = os.popen('stty size', 'r').read().split()
# print("Window Size: {} x {}".format(columns, rows)); time.sleep(3)

WIDTH = int(columns)
HEIGHT = int(rows)

def convertline(s, width=WIDTH-4, indent=0):
    ''' 把一长段文字，以60字符宽度分割，单词不被切割换行 '''
    ''' 用换行符 '\n' 插入进行分隔 '''
    linelist = []
    txt = ' ' * indent + s
    begin = 0
    end = 0
    while True:
        if begin + width > len(txt):
            linelist.append(txt[begin:])
            break
        end = txt.rfind(' ', begin, begin+width)
        linelist.append(txt[begin:end])
        begin = end + 1
    return linelist

def convertTxt(filePath):
    initLines = []; reslines = []
    wordCount = 0
    lineCount = 0
    with open(filePath) as fp:
        for line in fp.readlines():
            line = line.strip('\n');     wordCount += len(line.split())
            line_s = convertline(line);  lineCount += len(line_s)
            initLines.extend(line_s)
    # 获取最长行的字符数
    maxLen = 0
    for line in initLines:
        if len(line) > maxLen:
            maxLen = len(line)
    # 计算空格插入数量
    x = int( (WIDTH - maxLen) / 2 )
    # 生成新的 lines
    for line in initLines:
        reslines.append(' ' * x + line)
    return ('\n'.join(reslines), lineCount, wordCount)

def blit(s, wi=0.01, after=0.0):
    ''' 打印上面转换的文字， 单词间停顿， 连续不可见字符只停顿1次 '''
    # if empty_char after, wait is off
    switch = 1
    colorswitch = False

    for c in s:

        # color style starts with '['
        if c == '[':
            colorswitch = True
            c = ''
        # color style ends with ']'
        if c == ']':
            colorswitch = False
            c = ''

        if colorswitch:
            sys.stdout.write('\x1b[0;32;48m' + c + '\x1b[0m')
        else:
            sys.stdout.write(c)
        sys.stdout.flush()
        if c == ' ' or c == '\n' or c == '\t':
            if switch:
                switch = 0
                time.sleep(wi)
        else:
            switch = 1
    sys.stdout.write('\n')

def playText(fpath, sec_per_word):
    ''' 根据路径，播放文件 '''

#    threading.Thread(target=playStrokeSound, args=()).start() # play sound

    txt, lineCount, wordCount = convertTxt(fpath)

    # 播放
    emptylines = int( (HEIGHT - lineCount - 2) / 2 ); sys.stdout.write(emptylines*'\n')
    wordInterv = 0.7 / wordCount;  blit(txt, wi=wordInterv)
    sys.stdout.write(emptylines*'\n')

    info = " {} lines, {} words ".format(lineCount, wordCount).center(WIDTH, '~')
    space_pos = info.rfind(' ') + 1
    sys.stdout.write(info[:space_pos])
    restinfo = info[space_pos:]

    wait_time = wordCount * float(sec_per_word) + 2.5
    interv = wait_time / len(restinfo)
    for _ in restinfo:
        sys.stdout.write('~')
        time.sleep(interv)
        sys.stdout.flush()


def main():

    ## BASEDIR=os.path.dirname(__file__) + "/txtFiles/English/Vocabulary"
    BASEDIR=os.path.dirname(__file__) + "/Words/"

    print("Dirname:", os.path.dirname(__file__)); time.sleep(1.2)

    # Welcome Info
    os.system('clear')
    txt = convertTxt(os.path.dirname(__file__) + "/welcomeInfo")[0]
    print(" WELCOME! ".center(WIDTH, '~'))
    print(txt)
    print(WIDTH * '~')
    time.sleep(2.5)

    ## change dir, list dir
    if len(sys.argv) == 3:
        sec_per_word = sys.argv[1]
        DIR = sys.argv[2]
    elif len(sys.argv) == 2:
        sec_per_word = sys.argv[1]
        DIR = BASEDIR
    else:
        sec_per_word = 0.9
        DIR = BASEDIR

    os.chdir(DIR)

    ## open file, write, close
    #fp = open("t3.txt", 'w')
    #fp.write("hello")
    #fp.close()

    # 遍历，获取所有文件路径, 组成列表
    playlist = []
    for dr, folder, filelist in os.walk("."):
        for f in filelist:
            path = os.path.join(dr, f);
            playlist.append(path)
    # print(playlist); time.sleep(3)

    # 乱序列表， 播放
    random.shuffle(playlist)
    # play loop
    while True:
        for p in playlist:
            title = ' ' + os.path.basename(p) + ' '
            os.system("clear") # 清屏
            print(title.center(WIDTH, '~')) # 标题
            playText(p, sec_per_word) # 播放

if __name__ == "__main__":
    print(__file__)

#    pygame.mixer.init()
#    pygame.mixer.music.load('media/keystroke.wav')
    main()
#    pygame.quit()
