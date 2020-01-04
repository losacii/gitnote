import pyautogui as pag
import pyperclip
import time
import sys, os

if len(sys.argv) > 1:
    text = sys.argv[1]
else:
    text = 'Hello world!\n' * 3

print(f"PyAutoGui Version:{pag.__version__}".center(80, '-'))

pag.moveTo(530, 80)
pag.click()

print("Counting down:")
for i in range(3):
    print(3 - i)
    sys.stdout.flush()
    time.sleep(1)


pag.typewrite(text, interval=0.03)

# pyperclip.copy("It's leviOsa, not lêvioçÁ!")
# pag.hotkey("ctrl", "v")
