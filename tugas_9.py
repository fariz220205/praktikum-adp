import time
import os
from termcolor import colored, cprint

for gerak in range(30):
    os.system("cls")
    for i in range(3):
        maju_mundur = " " * ((gerak + i*2) % 6)
        cprint(maju_mundur + " " * 20,"white","on_red")
    for i in range(3):
        maju_mundur = " " * ((gerak + i*2) % 6)
        cprint( maju_mundur + " " * 20,"white","on_white")
    for i in range(9) :
        cprint(" ","white","on_white")
    time.sleep(0.5)