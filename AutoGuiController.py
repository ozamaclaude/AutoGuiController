import pyautogui
import webbrowser
import time

def Press(key):
    pyautogui.keyDown(key)
    pyautogui.keyUp(key)

def SendTab(menuTabCount):
    i = 0
    while i < menuTabCount:
        Press('tab')
        i += 1

#施設予約システム（うぐいすネット）起動 
webbrowser.open("https://www.yoyaku.city.ota.tokyo.jp/")

# 画面の起動状況を、全画面文字列コピーから検出できないか？
# ctrl + aで範囲指定し、コピーした後、クリップボードの内容を変数に設定するとか
pyautogui.sleep(20)
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
Press('pagedown')
sc = pyautogui.screenshot()
sc.save('test.png')

