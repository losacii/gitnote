import pyperclip

s = pyperclip.paste()
print(s)





'''

import pyautogui as pag
import pyperclip
import time
import sys, os


def operations():
    if len(sys.argv) > 1:
        text = sys.argv[1]
    else:
        text = 'Hello world!\n' * 3

    pz = pag.position()

    pag.moveTo(1300, 300)
    pag.click()
    for word in text.split(' '):
        pag.typewrite(word, interval=0.02);
        pag.typewrite(' ');
        time.sleep(0.07)
    pag.press('enter')

    pag.moveTo(pz)
    pag.click()

def op1():
    """Use Clipboard
    :returns: TODO

    """
    pag.moveTo(1300, 300)
    pag.click()

    pag.hotkey("ctrl",  "shift", "v")


if __name__ == "__main__":

    operations()
'''
