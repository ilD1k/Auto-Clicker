import keyboard
import mouse
import time

isClicking = False

def set_clicker():
    global isClicking
    if isClicking:
        isClicking = False
        print("Кликер не работает")
    else:
        isClicking = True
        print("Кликер работает как надо")





keyboard.add_hotkey("F6" , set_clicker)

while True:
    if isClicking:
        mouse.double_click(button = "left")
        time.sleep(0.01)