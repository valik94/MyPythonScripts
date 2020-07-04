#Gui Automation Section 16
#Controlling the mouse with python

import pyautogui

pyauthogui.size()
width, height = pyautogui.size()

#moving cursor to desired coordinates
pyautogui.moveTo(10,10) #(10,10,duration=5) duration is delay to move the mouse slowly
pyautogui.moveRel(200,0)    #(200,0,duration=2) move mouse to right
pyautogui.moveRel(0,-100)   #move mouse up by 100 pixels
pyautogui.click(19,42) #Use pyautogui.position() to find coordinates what you want to click
pyautogui.doubleClick(19,42) #double click
pyautogui.middleClick(19,42) #middle click

#pyautogui.dragRel(distance,0,duration=3)
#for examples refer to spiraldraw
#use command line
#run python -- python
#imnport pyautogui
#pyautogui.displayMousePosition()

#TYPING to window
pyautogui.typewrite('content of what you want to type')
#to run 2 windows at once... 1.clikc on window of focus to type into 2.typewrite into it
pyautogui.click(100,100) ; pyautogui.typewrite('Hello World', interval=0.2)
#typing and moving typing left twice
pyautogui.click(100,100) ; pyautogui.typewrite(['a','b','left','left','X','Y'],interval=1)
#for more keys Type: 'pyautogui.KEYBOARD_KEYS'
pyautogui.press('f1')
#for multiple keys use hotkey('key1','key2')
pyautogui.hotkey('ctrl','s')


#PILLOW LIBRARY VERY USEFUL - READ DOCS  
#Screenshots and saves to hard drive
pyautogui.screenshot('C:\\Users\\stars\\MyPythonScripts\\screenshot_example.jpg')
#Image recognition of 7 key on calculator (from image)- didn't work
pyautogui.locateOnScreen('C:\\Users\\stars\\MyPythonScripts\\calc7key.png')
#locating center of key
pyautogui.locateCenterOnScreen('C:\\Users\\stars\\MyPythonScripts\\calc7key.png')
