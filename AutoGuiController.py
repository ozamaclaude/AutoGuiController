import pyautogui
import webbrowser
import time

def SendTab(menuTabCount):
    i = 0
    while i < menuTabCount:
        pyautogui.keyDown('tab')
        pyautogui.keyUp('tab')
        i += 1
#施設予約システム（うぐいすネット）起動 
webbrowser.open("https://www.yoyaku.city.ota.tokyo.jp/")

pyautogui.sleep(5)
# tab ×　13回
menuTabCount = 13
SendTab(menuTabCount)

pyautogui.sleep(3)
pyautogui.press('enter')

# 利用目的選択
pyautogui.sleep(8)

menuTabCount = 56
SendTab(menuTabCount)

pyautogui.sleep(3)
pyautogui.press('enter')

pyautogui.sleep(3)
pyautogui.keyDown('pagedown')
pyautogui.keyUp('pagedown')
sc = pyautogui.screenshot()
sc.save('test.png')

