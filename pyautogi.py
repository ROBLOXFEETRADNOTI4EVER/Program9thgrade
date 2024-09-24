import pyautogui
import random
from time import sleep
import time

for bbc in range(5):
    x = random.randint(200,1400)
    sleep(0.2)
    y = random.randint(400,800)
    pyautogui.click(x,y)
    pyautogui.moveTo(y,x)
    pyautogui.moveRel(800,300)
