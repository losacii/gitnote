import pyautogui as pag
import pyperclip
import time
import sys, os


def operations():

    # Text From Clipboard
    text = pyperclip.paste() 

    pz = pag.position()
    pag.moveTo(520, 44)
    pag.click()

    # time count
    # for i in range(2):
        # print(2-i)
        # sys.stdout.flush()
        # time.sleep(0.8)

    # input with animation
    pos = 0; start = 0
    checker = []
    for ch in text:
        checker.append(ch)
        if len(checker) > 2:
            checker.pop(0)
            if checker[1] == ' ' and checker[0] is not ' ':
                pag.typewrite(text[start:pos], interval=0.01); time.sleep(0.03)
                start = pos
        pos += 1
    pag.typewrite(text[start:], interval=0.01);

    pag.moveTo(pz)
    #pag.click()

def op1():
    """Use Clipboard
    :returns: TODO

    """
    pag.moveTo(1300, 300)
    pag.click()

    pag.hotkey("ctrl",  "shift", "v")


if __name__ == "__main__":

    operations()
