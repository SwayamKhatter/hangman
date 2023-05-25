from pyautogui import press, typewrite, click, position, hotkey
from time import sleep

def bakkesmod():
    press('win')
    typewrite('BakkesMod')
    press('enter', interval=1.0)
    print('BAKKESMOD LAUNCHED')
    
def rl():
    hotkey('win', 'r')
    typewrite('ask godson what to put here', interval=0.01)
    press('enter', interval=1.0)
    press('enter', interval=0.5)
    print('Rocket League Launching...')

print('Launching...')
bakkesmod()
press('enter')
sleep(1)
hotkey('win', 'm')
sleep(3)
rl()
hotkey('win', 'm')