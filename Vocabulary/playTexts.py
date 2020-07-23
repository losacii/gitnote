#\ coding:utf-8
import os, sys
import time
import random
import re
import codecs

#import threading
#import pygame
#
#def playStrokeSound():
#    pygame.mixer.music.play()
#    while pygame.mixer.music.get_busy(): 
#        pygame.time.Clock().tick(10)


# terminal width, height
rows, columns = os.popen('stty size', 'r').read().split()
# print("Window Size: {} x {}".format(columns, rows)); time.sleep(3)

TERM_WIDTH = int(columns)
TERM_HEIGHT = int(rows)

def convertline(s, width=TERM_WIDTH-4, indent=0):
    ''' convert a long line to trimmed lines, in a list'''
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

def separateFile(fp): # to texts
    f = codecs.open(fp, encoding="utf8")
    texts = f.read().split("\r\n\r\n>>>\r\n")
    f.close()
    return texts

def blit(s, wi=0.01, after=0.0):
    ''' play a string '''
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
    sys.stdout.flush()

def playTexts(texts, sec_per_word):

    if len(sys.argv) >= 2:
        sec_per_word = float(sys.argv[1])
    print("Terminal height:", TERM_HEIGHT, "argCount:", len(sys.argv))
    time.sleep(3)

    for text in texts:
        initLines = []; reslines = []
        wordCount = 0
        lineCount = 0
        lines = text.split("\n")

        for line in lines:
            line = line.strip('\n');     wordCount += len(line.split())
            line_s = convertline(line);  lineCount += len(line_s)
            initLines.extend(line_s)

        # 获取最长行的字符数
        maxLen = 0
        for line in initLines:
            if len(line) > maxLen:
                maxLen = len(line)
        # 计算空格插入数量
        x = int( (TERM_WIDTH - maxLen) / 2 )
        # 生成新的 lines
        for line in initLines:
            reslines.append(' ' * x + line)

        # threading.Thread(target=playStrokeSound, args=()).start() # play sound

        os.system("clear")
        print(int(TERM_WIDTH / 2) * "~ ")
        txt= '\n'.join(reslines)
        # 播放
        emptylines = int( (TERM_HEIGHT - lineCount) / 2 )
        emptylines -= 1

        sys.stdout.write((emptylines)*'\n')
        wordInterv = 0.7 / wordCount;  blit(txt, wi=wordInterv)
        if (TERM_HEIGHT - lineCount) % 2 != 0:
            sys.stdout.write('\n')
        sys.stdout.write(emptylines*'\n')

        info = " {} lines, {} words ".format(lineCount, wordCount).center(TERM_WIDTH, '~')
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
    BASEDIR=os.path.dirname(__file__)

    # Welcome Info
    # os.system('clear')

    filepath = os.path.join(BASEDIR, "TextFiles", "tmp.txt")
    texts = separateFile(filepath)
    random.shuffle(texts)
    playTexts(texts, 0.02)


if __name__ == "__main__":
    #res = re.split(">+", "hello>>>woord>>nice")
    #print(res)

#    pygame.mixer.init()
#    pygame.mixer.music.load('media/keystroke.wav')
    main()
#    pygame.quit()
