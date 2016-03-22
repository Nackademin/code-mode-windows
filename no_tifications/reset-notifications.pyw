# -*- coding: utf-8 -*-

import win32api
import win32con
import win32gui
import time
from _winreg import *

#Returns True if notifications are turned on in Windows.
def isNotificationsOn():
	aReg = ConnectRegistry(None,HKEY_CURRENT_USER)
	aKey = OpenKey(aReg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Notifications\Settings")
	try:
		str = EnumValue(aKey,0)
		return False
	except:
		return True
		
#Toggles notifications On/Off.
def toggleNotifications(activeWindow,meddelandecenter):
	#Send a command to the window to activate the menu (turn on manually by using right click)
	win32api.SendMessage(meddelandecenter, win32con.WM_CONTEXTMENU, meddelandecenter,0)
			
	for i in range(0,20): #Try to find the menu 20 times before proceeding.
		menu = win32gui.FindWindow("#32768",None) #The menu window we opened.
		time.sleep(delay)
		if menu > 0:
			break
	
	if menu <= 0:
		print("Kunde inte aktivera menyn")
		return
	#Find the menus position
	dim = win32gui.GetWindowRect(menu)
	x = (dim[0]+dim[2])/2
	y = dim[3]-15
	#Simulate a click on the bottom half of the menu.
	click(x,y)
	time.sleep(delay)
	#Reset focus to Sublime.
	if activeWindow>1:
		win32gui.SetForegroundWindow(activeWindow)

#Simulate a click by the coordinates.
def click(x,y):
	old = win32api.GetCursorPos()
	win32api.SetCursorPos((x,y))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
	win32api.SetCursorPos(old)
	
#Find the notification center window.
def findMessageCenter():
	taskbar = win32gui.FindWindow("Shell_TrayWnd",None) #Taskbar-window in Windows.
	subtaskbar = win32gui.FindWindowEx(taskbar,None,"TrayNotifyWnd",None) #The right part window by the taskbar where e.g. The clock is showing.
	meddelandecenter = win32gui.FindWindowEx(subtaskbar,None,"TrayButton",None) #Notification center window.
	#To find the name of the other windows in Windows you can use tools as "Windows detective" or "Spy++".
	return meddelandecenter

delay = 0.06
#Turn on notifcations if turned off.
if isNotificationsOn()==False:
	toggleNotifications(win32gui.GetForegroundWindow(),findMessageCenter())

