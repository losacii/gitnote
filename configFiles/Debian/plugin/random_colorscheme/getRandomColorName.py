import os
import sys
import random

if sys.argv[1] == "dark":
    colorDIR = "/home/vi/.vim/colors/dark/"
if sys.argv[1] == "light":
    colorDIR = "/home/vi/.vim/colors/light/"

colors = os.listdir(colorDIR)

color = random.choice(colors)
rcolor = colorDIR + color

os.sys.stdout.write(rcolor)
