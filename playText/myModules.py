import os
import sys

# 获取当前终端的宽度和高度
rows, columns = os.popen('stty size', 'r').read().split()
print("terminal rows: {}, columns: {}".format(rows, columns))

TERM_WIDTH = int(columns) # 宽度
TERM_HEIGHT = int(rows) # 高度

def blitString(s, indent=2, hpad=2):
    sys.stdout.write(' ' * (hpad + indent))
    l = hpad + indent;
    words = s.split(' ')
    for word in words[:-1]:
        if l + len(word) >= TERM_WIDTH - hpad:
            sys.stdout.write('\n' + ' ' * hpad)
            l = len(word) + 1 + hpad
        else:
            l += len(word) + 1
        sys.stdout.write(word + ' ')
    sys.stdout.write(words[-1])

def blitLines():
    pass

if __name__ == "__main__":
    s = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua." * 5

    print(' ~' * (TERM_WIDTH // 2))

    for line in open("./lorem", "r"):
        blitString(line)


    print('\n' + ' ~' * (TERM_WIDTH // 2))
