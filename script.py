import cv2
import pyautogui
from time import sleep
from PIL import Image

region=(57, 125, 1517, 855)

def foundTinted():
    pyautogui.click(x=1752, y=1006)
    pyautogui.write('!tinted')  
    #pyautogui.press('enter')
    sleep (30)

while True:

    sleep(0.5)
    tinted = pyautogui.locateOnScreen('01.png', region=region, grayscale=True, confidence=0.9)

    if tinted:
        print ('tinted: 01', tinted)
        foundTinted()

    sleep(0.5)
    tinted = pyautogui.locateOnScreen('02.png', region=region, grayscale=True, confidence=0.9)

    if tinted:
        print ('tinted: 02', tinted)
        foundTinted()

    sleep(0.5)
    tinted = pyautogui.locateOnScreen('03.png', region=region, grayscale=True, confidence=0.9)

    if tinted:
        print ('tinted: 03', tinted)
        foundTinted()

    sleep(0.5)
    tinted = pyautogui.locateOnScreen('04.png', region=region, grayscale=True, confidence=0.9)

    if tinted:
        print ('tinted: 04', tinted)
        foundTinted()