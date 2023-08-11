import pyautogui
import time
time.sleep(2)
count = 0
while count<=10:
    pyautogui.typewrite("HELLO")
    time.sleep(1)
    pyautogui.press("enter")
    count = count +1