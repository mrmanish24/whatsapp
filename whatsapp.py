import pyautogui
import time
time.sleep(4)
count= 0
while count <=100:
    pyautogui.typewrite(f"Hello {count}")
    time.sleep(1)
    pyautogui.press("enter")
    count+=1

