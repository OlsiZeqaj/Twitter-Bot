import time
import random
import pyautogui

Prompts = [""]
Prompt = Prompts[0]

#Time For Setup
time.sleep(5)

#Launch ChatGPT And Twitter
pyautogui.write("https://chat.openai.com/")
pyautogui.press("enter")
time.sleep(5)
pyautogui.hotkey("ctrl", "t")
pyautogui.write("https://twitter.com/home")
pyautogui.press("enter")
time.sleep(5)

while True:
    #Generate Tweet
    pyautogui.hotkey("ctrl", "shift", "tab")
    pyautogui.click(1100, 1350)
    pyautogui.write(Prompt)
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(5)
    CopyButton = pyautogui.locateCenterOnScreen("CopyButton.png")
    pyautogui.click(CopyButton)
    time.sleep(1)

    #Click On Tweet Button
    pyautogui.hotkey("ctrl", "tab")
    TweetButton = pyautogui.locateCenterOnScreen("TweetButton.png")
    pyautogui.click(TweetButton)
    time.sleep(1)

    #Post Tweet
    pyautogui.hotkey("ctrl", "v")
    time.sleep(1)
    pyautogui.hotkey("ctrl", "enter")
    time.sleep(30)

    Prompt = random.choice(Prompts)
