#!/usr/bin/env python3
import time
from random import randint
import sys

def randomDots():
    num = randint(0, 2 * 80)
    for i in range(num):
        sys.stdout.write(".")
        sys.stdout.flush()
    sys.stdout.write("\n")
    sys.stdout.flush()

while True:
    randomDots()
    time.sleep(0.03)
    
#
