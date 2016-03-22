# -*- coding: utf-8 -*-

import pyttsx
import win32gui
import time

engine = pyttsx.init() #Initiate the text-to-speech engine.
timer = 0 # Time spent on entertainment sites.
timeCap = 5*60 #Time in seconds before a text message is played.
list = ["Facebook", "YouTube", "reddit"] #List of entertainment site.
while True:
	active = win32gui.GetWindowText(win32gui.GetForegroundWindow()) #Active window.
	
	#Check if the active window is one of the entertainment sites.
	inList=False
	for x in list:
		if x in active:
			inList=True
			break

			
	#Increase timer if it was one of the entertainment sites in the list.
	if inList:
		timer+=1
		#Display a warning if we've been active on the sites for 5 minutes.
		if timer>timeCap:
			engine.say('You are losing your flow. Go back to coding.')
			engine.runAndWait()
			timer=0
	else:
		#Decrease the timer if we haven't been active on any of the sites.
		timer-=1
		if timer < 0:
			timer=0
			
	#Wait a second.
	time.sleep(1)