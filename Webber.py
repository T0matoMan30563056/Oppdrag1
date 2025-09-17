import webbrowser
import pyautogui
import time
import keyboard

while True:
    if keyboard.is_pressed("q"):
        print("Stopped.")
        break
    
    webbrowser.open("https://www.youtube.com/")
    time.sleep(2)
    

    if keyboard.is_pressed("q"): break
    xPos = 1920/3
    yPos = 1080/100 * 20 
    # Move
    pyautogui.moveTo(xPos, yPos, duration=0)

    # Click
    time.sleep(0.5)
    if keyboard.is_pressed("q"): break
    pyautogui.click()

    if keyboard.is_pressed("q"): break
    pyautogui.typewrite("Rick Roll", interval=0)
    pyautogui.press("enter")

    
    time.sleep(1)

    pyautogui.moveRel(10, 200, duration=0)
    pyautogui.click()












