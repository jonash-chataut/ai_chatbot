import pyautogui
import time
import pyperclip
# from openai import OpenAI
import re

# Give some time to switch to the right window
time.sleep(20)

 # Step 1: Click on the icon
# pyautogui.click(1046, 1048)
# time.sleep(2)  # Wait for the application to open

# pyautogui.click(840, 969)

haha_text="Haha"
haha_text1="😂😂"
haha_emo="🙄🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣🙄🙄😒😒😒😒"
while True:
    # haha_text="Haha"
    # pyautogui.click(840, 969)
    # time.sleep(1)
    pyperclip.copy(haha_text)
    pyautogui.hotkey("ctrl", "v")

    # time.sleep(1)
    pyautogui.press("enter")
    # time.sleep(1)
    # haha_text1="😂😂"
    pyperclip.copy(haha_text1)
    pyautogui.hotkey("ctrl", "v")

    # time.sleep(1)
    pyautogui.press("enter")
    # wait for 30 second after sending reply
    # time.sleep(1)

    # haha_emo1="😒＞︿＜🙄"
    # haha_emo="🙄🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣🙄🙄😒😒😒😒"
    # pyautogui.click(840, 969)
    # time.sleep(1)
    pyperclip.copy(haha_emo)
    pyautogui.hotkey("ctrl", "v")

    # time.sleep(1)
    pyautogui.press("enter")
    # time.sleep(5)
    # pyperclip.copy(haha_emo1)
    # pyautogui.hotkey("ctrl", "v")
    # time.sleep(1)
    # pyautogui.press("enter")
    # wait for 30 second after sending reply
    # time.sleep(0.5)🙄🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣🙄🙄😒😒😒😒
    
    

