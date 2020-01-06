import pyautogui as pag
import pyperclip
import time
import sys, os


def operations():
    if len(sys.argv) > 1:
        text = sys.argv[1]
    else:
        text = 'Hello world!\n' * 3

    pag.moveTo(1300, 300)
    pag.click()

    pag.typewrite(text, interval=0.03)
    # pag.press('enter')

def op1():
    """Use Clipboard
    :returns: TODO

    """
    pag.moveTo(1300, 300)
    pag.click()

    #pyperclip.copy("It's leviOsa, not lêvioçÁ!")
    pag.hotkey("ctrl",  "shift", "v")


if __name__ == "__main__":
    p0 = pag.position()

    #operations()
    op1()

    pag.moveTo(p0)
    pag.click()
    time.sleep(0.4)
    pag.press('space')

