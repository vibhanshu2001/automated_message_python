#Automated text messaging

import time
import pyautogui

def SendMessage():
    time.sleep(2)
    text = open('script.txt')
    for each_line in text:
        pyautogui.typewrite(each_line)
        pyautogui.press('enter')
SendMessage()
