# coding:utf-8
import os, sys

# 获取当前终端的宽度和高度
rows, columns = os.popen('stty size', 'r').read().split()

TERM_WIDTH = int(columns) # 宽度
TERM_HEIGHT = int(rows) # 高度

def blit2(s):
    l = 0
    words = s.split(' ')
    for word in words:
        if l + len(word) >= TERM_WIDTH:
            sys.stdout.write('\n')
            l = len(word) + 1
        else:
            l += len(word) + 1
        sys.stdout.write(word + ' ')



if __name__ == "__main__":
    print(TERM_WIDTH)
    blit2("hello world! " * 40)
