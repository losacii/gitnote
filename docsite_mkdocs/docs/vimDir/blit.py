import os
import sys
import time
from random import random

def blit(*stringlist):
    """blit info"""
    for s in stringlist:
        for char in s:
            if random() < 0.3:
                time.sleep(0.2)
            sys.stdout.write(char)
            sys.stdout.flush()
    
if __name__ == '__main__':
    blit("hello ", "world!", "\nNice to see you!")
    blit()
