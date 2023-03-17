# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
'''
import pyautogui as PA
import time
import PIL

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    for i in range(12):
        time.sleep(5)
        PA.moveTo(519,328,duration=3)
        PA.doubleClick()
        time.sleep(10)
        print("duoble click")                                                                                 
        time.sleep(300)
        PA.doubleClick()
        print("duoble click")
        time.sleep(60)
        PA.moveTo(519,300,duration=3)
        time.sleep(300)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
'''

import sys

sys.stdin = open("./algo/input.txt","rt")
a = list(input() for _ in range(181))
print(','.join(x for x in a))
pass