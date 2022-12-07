# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pyautogui as PA
import time

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while True:
        time.sleep(5)
        PA.moveTo(-2790,50,duration=3)
        PA.doubleClick()
        time.sleep(10)
        print("duoble click")                                                                                 
        time.sleep(300)
        PA.doubleClick()
        print("duoble click")
        time.sleep(60)
        PA.moveTo(-2790,32,duration=3)
        time.sleep(300)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
