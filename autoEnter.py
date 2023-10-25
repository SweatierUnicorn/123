import pyautogui
from PIL import Image, ImageChops
import time
from playsound import playsound
import random

playsound('C:/Users/hhyma/Desktop/py/tap.ogg')


time.sleep(1)
topLineIMG = pyautogui.screenshot("topLineIMG.png", region=(0, 0, 1920, 25))
backToMainMenuButtonIMG = pyautogui.screenshot("backToMainMenuButtonIMG.png", region=(954, 696, 608, 68))
cancelButtonIMG = pyautogui.screenshot("cancelButton.png", region=(939, 711, 615, 67))

topLineIMG = Image.open('C:/Users/hhyma/Desktop/py/topLineIMG.png')
backToMainMenuButtonIMG = Image.open('C:/Users/hhyma/Desktop/py/backToMainMenuButtonIMG.png')
cancelButtonIMG = Image.open('C:/Users/hhyma/Desktop/py/cancelButton.png')


def clickSound():
    playsound('C:/Users/hhyma/Desktop/py/clickSound.wav')


def reConnect(x, y):
    # Click to button - back to main menu or cancel button
    pyautogui.moveTo(x, y)
    clickSound()
    pyautogui.click()

    # Open Servers List
    time.sleep(2)
    pyautogui.moveTo(650, 451)
    pyautogui.keyDown('shift')
    clickSound()
    pyautogui.click()
    pyautogui.keyUp('shift')

    # Connect To Server
    time.sleep(2)
    pyautogui.moveTo(1238, 524)
    clickSound()
    pyautogui.click(clicks=2)


while True:
    # time.sleep(random.randint(60, 400))
    if (pyautogui.locateOnScreen(topLineIMG) != None):
        if (pyautogui.locateOnScreen(backToMainMenuButtonIMG)):
            print("HIT!")
            reConnect(951, 600)

        if (pyautogui.locateOnScreen(cancelButtonIMG) != None):
            playsound('C:/Users/hhyma/Desktop/py/pam.wav')
            time.sleep(60)  # wait 1 min
            if (pyautogui.locateOnScreen(cancelButtonIMG) != None):
                reConnect(933, 677)
