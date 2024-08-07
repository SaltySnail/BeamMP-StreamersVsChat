import socket
import threading
# from ahk import AHK #auto hotkey
import time
import json #to write data file
import os #check file size
import vlc #sound effects

#Download Autohotkey at https://www.autohotkey.com/ and provide the address to
#AutoHotkey.exe below!
# ahk = AHK(executable_path='C:\\Program Files\\AutoHotkey\\v2\\AutoHotkey.exe')

SERVER = "irc.twitch.tv"
PORT = 80

PASS = "" #make empty global variable
#Your OAUTH Code Here https://twitchapps.com/tmi/
with open("DONTOPENMEWHILELIVE.oauth", "r") as file: #must contain the code gathered from the above site.
	PASS = file.read()
	file.close

#What you'd like to name your bot
BOT = "JulianstapTwitchBot"

#The channel you want to monitor
CHANNEL = "Julianstap"

#Your account
OWNER = "Julianstap"

irc = socket.socket()

irc.connect((SERVER, PORT))
irc.send((	"PASS " + PASS + "\n" +
			"NICK " + BOT + "\n" +
			"JOIN #" + CHANNEL + "\n").encode())

BEAMMP_SERVER_EXE_FOLDER = "C:/Users/Julian/Desktop/beammp_Server/windows"

PRESS_TIME = 0.5 #s
SHORT_COOLDOWN = 120 #s

BEAMNGCOMMANDS = [
					{	#use honk as an example for a command which triggers two commands and has no sound effect
						"command":"honk",
						"waitingOnEndOfSound":False, #don't change this variable, this is used for logic
						"caseSensitive":False,
						"pressTime":PRESS_TIME,
						"cooldown":SHORT_COOLDOWN,
						"cooldownEndTime":time.time(), #don't change this variable, this is used for logic
						"hasSecondFunction":True,
						"hasSound":False,
						"beamng":True,
						"hasThirdFunction":False,
						"beamCommand":"honk",
						"argument":"nil",						
						"extraFunctions":{
							"0":{
								"beamng":True,
								"beamCommand":"stopHonk",
								"argument":"nil",
								"endTime":100000000000 #don't change this variable, this is used for logic
							}
						}
					},
					{	#use siren as an example for a command which triggers one command and has no sound effect
						"command":"siren",
						"waitingOnEndOfSound":False, #don't change this variable, this is used for logic
						"caseSensitive":False,
						"pressTime":PRESS_TIME,
						"cooldown":SHORT_COOLDOWN,
						"argument":"nil",
						"cooldownEndTime":time.time(), #don't change this variable, this is used for logic
						"hasSecondFunction":False,
						"hasSound":False,
						"beamng":True,
						"hasThirdFunction":False,
						"beamCommand":"siren"
					},
					{	
						"command":"brake",
						"waitingOnEndOfSound":False, #don't change this variable, this is used for logic
						"caseSensitive":False,
						"pressTime":PRESS_TIME,
						"cooldown":SHORT_COOLDOWN,
						"cooldownEndTime":time.time(), #don't change this variable, this is used for logic
						"hasSecondFunction":True,
						"hasSound":False,
						"beamng":True,
						"hasThirdFunction":False,
						"beamCommand":"brake",
						"argument":"nil",						
						"extraFunctions":{
							"0":{
								"beamng":True,
								"beamCommand":"stopBrake",
								"argument":"nil",
								"endTime":100000000000 #don't change this variable, this is used for logic
							}
						}
					},
					{	
						"command":"gas",
						"waitingOnEndOfSound":False, #don't change this variable, this is used for logic
						"caseSensitive":False,
						"pressTime":PRESS_TIME,
						"cooldown":SHORT_COOLDOWN,
						"cooldownEndTime":time.time(), #don't change this variable, this is used for logic
						"hasSecondFunction":True,
						"hasSound":False,
						"beamng":True,
						"hasThirdFunction":False,
						"beamCommand":"gas",
						"argument":"nil",
						"secondFunction":{
							"beamng":True,
							"beamCommand":"stopGas",
							"argument":"nil",
							"endTime":100000000000 #don't change this variable, this is used for logic
						}
					},
					{
						"command":"And his name is... JOHN CENA!!!",
						"waitingOnEndOfSound":False, #don't change this variable, this is used for logic
						"caseSensitive":True,
						"pressTime":1,
						"cooldown":1800, #30 minutes
						"cooldownEndTime":time.time(), #don't change this variable, this is used for logic
						"hasSecondFunction":True,
						"hasSound":True,
						"delayAfterSound":0.1,
						"soundDelayEndTime":0, #don't change this variable, this is used for logic
						"soundName":"JOHNCENA",
						# "sound":{ #sound effects are now done in beamng, so that everyone hears them
						# 	"delay":0,
						# 	"endTime":time.time(), #don't change this variable, this is used for logic
						# 	"filename":"JOHNCENA.mp3",
						# 	"volume":80
						# },
						"beamng":True,
						"hasThirdFunction":True,
						"beamCommand":"johncena",
						"argument":"nil",
						"extraFunctions":{
							"0":{
								"beamng":True,
								"beamCommand":"hop",
								"argument":"20",
								"delay":1,
								"endTime":100000000000 #don't change this variable, this is used for logic
							},
							"1":{
								"beamng":True,
								"beamCommand":"hop",
								"argument":"-40",
								"endTime":100000000000 #don't change this variable, this is used for logic
							}
						}
					},
					{
						"command":"boost",
						"waitingOnEndOfSound":False, #don't change this variable, this is used for logic
						"caseSensitive":False,
						"pressTime":PRESS_TIME,
						"cooldown":45,
						"cooldownEndTime":time.time(), #don't change this variable, this is used for logic
						"hasSecondFunction":False,
						# "hasSound":False, #implemented in VE lua
						"beamng":True,
						"hasThirdFunction":False,
						# "sound":{
						# 	"delay":0,
						# 	"endTime":time.time(), #don't change this variable, this is used for logic
						# 	"filename":"GASGASGAS.mp3",
						# 	"volume":80
						# },
						"hasSound":True,
						"delayAfterSound":0.1,
						"soundDelayEndTime":0, #don't change this variable, this is used for logic
						"soundName":"GASGASGAS",
						"beamCommand":"boost",
						"argument":"5"
					},
					{
						"command":"boost backwards",
						"waitingOnEndOfSound":False, #don't change this variable, this is used for logic
						"caseSensitive":False,
						"pressTime":PRESS_TIME,
						"cooldown":SHORT_COOLDOWN,
						"cooldownEndTime":time.time(), #don't change this variable, this is used for logic
						"hasSecondFunction":False,
						"hasSound":False,
						"beamng":True,
						"hasThirdFunction":False,
						"beamCommand":"boost",
						"argument":"-10"
					},
					{	
						"command":"handbrake",
						"waitingOnEndOfSound":False, #don't change this variable, this is used for logic
						"caseSensitive":False,
						"pressTime":PRESS_TIME,
						"cooldown":SHORT_COOLDOWN,
						"cooldownEndTime":time.time(), #don't change this variable, this is used for logic
						"hasSecondFunction":True,
						"hasSound":False,
						"beamng":True,
						"hasThirdFunction":False,
						"beamCommand":"handbrake",
						"argument":"nil",						
						"extraFunctions":{
							"0":{
								"beamng":True,
								"beamCommand":"stopHandbrake",
								"argument":"nil",
								"endTime":100000000000 #don't change this variable, this is used for logic
							}
						}
					},
					{
						"command":"i'm blind",
						"waitingOnEndOfSound":False, #don't change this variable, this is used for logic
						"caseSensitive":False,
						"pressTime":3, #sound effect is 3 seconds long
						"cooldown":600,
						"cooldownEndTime":time.time(), #don't change this variable, this is used for logic
						"hasSecondFunction":True,
						# "hasSound":False, #implemented in VE lua
						"beamng":True,
						"hasThirdFunction":False,
						# "sound":{
						# 	"delay":0,
						# 	"endTime":time.time(), #don't change this variable, this is used for logic
						# 	"filename":"blind.mp3",
						# 	"volume":100
						# },
						"hasSound":True,
						"delayAfterSound":1,
						"soundDelayEndTime":0, #don't change this variable, this is used for logic
						"soundName":"blind",
						"beamCommand":"screenRGB",
						"argument":"0 0 0",						
						"extraFunctions":{
							"0":{
								"beamng":True,
								"beamCommand":"stopScreenRGB",
								"argument":"0 0 0",
								"endTime":100000000000 #don't change this variable, this is used for logic
							}
						}
					},
					{
						"command":"look back",
						"waitingOnEndOfSound":False, #don't change this variable, this is used for logic
						"caseSensitive":False,
						"pressTime":PRESS_TIME,
						"cooldown":SHORT_COOLDOWN,
						"cooldownEndTime":time.time(), #don't change this variable, this is used for logic
						"hasSecondFunction":True,
						"hasSound":False,
						"beamng":True,
						"hasThirdFunction":False,
						"beamCommand":"lookBack",
						"argument":"nil",						
						"extraFunctions":{
							"0":{
								"beamng":True,
								"beamCommand":"stopLookBack",
								"argument":"nil",
								"endTime":100000000000 #don't change this variable, this is used for logic
							}
						}
					},
					{
						"command":"moon",
						"waitingOnEndOfSound":False, #don't change this variable, this is used for logic
						"caseSensitive":False,
						"pressTime":1,
						"cooldown":SHORT_COOLDOWN,
						"cooldownEndTime":time.time(), #don't change this variable, this is used for logic
						"hasSecondFunction":True,
						"hasSound":False,
						"beamng":True,
						"hasThirdFunction":False,
						"beamCommand":"moon",
						"argument":"nil",						
						"extraFunctions":{
							"0":{
								"beamng":True,
								"beamCommand":"earth",
								"argument":"nil",
								"endTime":100000000000 #don't change this variable, this is used for logic
							}
						}
					},
					{
						"command":"clutch",
						"waitingOnEndOfSound":False, #don't change this variable, this is used for logic
						"caseSensitive":False,
						"pressTime":PRESS_TIME,
						"cooldown":SHORT_COOLDOWN,
						"cooldownEndTime":time.time(), #don't change this variable, this is used for logic
						"hasSecondFunction":True,
						"hasSound":False,
						"beamng":True,
						"hasThirdFunction":False,
						"beamCommand":"clutch",
						"argument":"nil",						
						"extraFunctions":{
							"0":{
								"beamng":True,
								"beamCommand":"stopClutch",
								"argument":"nil",
								"endTime":100000000000 #don't change this variable, this is used for logic
							}
						}
					},
					{
						"command":"drift",
						"waitingOnEndOfSound":False, #don't change this variable, this is used for logic
						"caseSensitive":False,
						"pressTime":PRESS_TIME,
						"cooldown":2400,
						"cooldownEndTime":time.time(), #don't change this variable, this is used for logic
						"hasSecondFunction":True,
						# "hasSound":False, #implemented in VE lua
						# "sound":{
						# 	"delay":0,
						# 	"endTime":time.time(), #don't change this variable, this is used for logic
						# 	"filename":"tokyo.mp3",
						# 	"volume":100
						# },
						"hasSound":True,
						"delayAfterSound":0.1,
						"soundDelayEndTime":0, #don't change this variable, this is used for logic
						"soundName":"tokyo",
						"beamng":True,
						"hasThirdFunction":False,
						"beamCommand":"drift",
						"argument":"nil",						
						"extraFunctions":{
							"0":{
								"beamng":True,
								"beamCommand":"stopDrift",
								"argument":"nil",
								"endTime":100000000000 #don't change this variable, this is used for logic
							}
						}
					},
					{
						"command":"look left",
						"waitingOnEndOfSound":False, #don't change this variable, this is used for logic
						"caseSensitive":False,
						"pressTime":PRESS_TIME,
						"cooldown":SHORT_COOLDOWN,
						"cooldownEndTime":time.time(), #don't change this variable, this is used for logic
						"hasSecondFunction":True,
						"hasSound":False,
						"beamng":True,
						"hasThirdFunction":False,
						"beamCommand":"lookLeft",
						"argument":"nil",						
						"extraFunctions":{
							"0":{
								"beamng":True,
								"beamCommand":"stopLookLeft",
								"argument":"nil",
								"endTime":100000000000 #don't change this variable, this is used for logic
							}
						}
					},
					{
						"command":"look right",
						"waitingOnEndOfSound":False, #don't change this variable, this is used for logic
						"caseSensitive":False,
						"pressTime":PRESS_TIME,
						"cooldown":SHORT_COOLDOWN,
						"cooldownEndTime":time.time(), #don't change this variable, this is used for logic
						"hasSecondFunction":True,
						"hasSound":False,
						"beamng":True,
						"hasThirdFunction":False,
						"beamCommand":"lookRight",
						"argument":"nil",						
						"extraFunctions":{
							"0":{
								"beamng":True,
								"beamCommand":"stopLookRight",
								"argument":"nil",
								"endTime":100000000000 #don't change this variable, this is used for logic
							}
						}
					},
					{
						"command":"right",
						"waitingOnEndOfSound":False, #don't change this variable, this is used for logic
						"caseSensitive":False,
						"pressTime":PRESS_TIME,
						"cooldown":SHORT_COOLDOWN,
						"cooldownEndTime":time.time(), #don't change this variable, this is used for logic
						"hasSecondFunction":True,
						"hasSound":False,
						"beamng":True,
						"hasThirdFunction":False,
						"beamCommand":"steerRight",
						"argument":"nil",						
						"extraFunctions":{
							"0":{
								"beamng":True,
								"beamCommand":"stopSteerRight",
								"argument":"nil",
								"endTime":100000000000 #don't change this variable, this is used for logic
							}
						}
					},
					{
						"command":"left",
						"waitingOnEndOfSound":False, #don't change this variable, this is used for logic
						"caseSensitive":False,
						"pressTime":PRESS_TIME,
						"cooldown":SHORT_COOLDOWN,
						"cooldownEndTime":time.time(), #don't change this variable, this is used for logic
						"hasSecondFunction":True,
						"hasSound":False,
						"beamng":True,
						"hasThirdFunction":False,
						"beamCommand":"steerLeft",
						"argument":"nil",						
						"extraFunctions":{
							"0":{
								"beamng":True,
								"beamCommand":"stopSteerLeft",
								"argument":"nil",
								"endTime":100000000000 #don't change this variable, this is used for logic
							}
						}
					},
					{
						"command":"ignition",
						"waitingOnEndOfSound":False, #don't change this variable, this is used for logic
						"caseSensitive":False,
						"pressTime":PRESS_TIME,
						"cooldown":SHORT_COOLDOWN,
						"cooldownEndTime":time.time(), #don't change this variable, this is used for logic
						"hasSecondFunction":True,
						"hasSound":False,
						"beamng":True,
						"hasThirdFunction":False,
						"beamCommand":"ignitionOff",
						"argument":"nil",						
						"extraFunctions":{
							"0":{
								"beamng":True,
								"beamCommand":"ignitionOn",
								"argument":"nil",
								"endTime":100000000000 #don't change this variable, this is used for logic
							}
						}
					},
					{
						"command":"ice ice baby",
						"waitingOnEndOfSound":False, #don't change this variable, this is used for logic
						"caseSensitive":False,
						"pressTime":3,
						"cooldown":660,
						"cooldownEndTime":time.time(), #don't change this variable, this is used for logic
						"hasSecondFunction":True,
						"hasSound":True,
						"delayAfterSound":1,
						"soundDelayEndTime":0, #don't change this variable, this is used for logic
						"soundName":"iceIceBaby",
						"beamng":True,
						"hasThirdFunction":False,
						"beamCommand":"ice",
						"argument":"nil",						
						"extraFunctions":{
							"0":{
								"beamng":True,
								"beamCommand":"stopIce",
								"argument":"nil",
								"endTime":100000000000 #don't change this variable, this is used for logic
							}
						}
					},
					{
						"command":"DO A BARREL ROLL!", 
						"waitingOnEndOfSound":False, #don't change this variable, this is used for logic
						"caseSensitive":True,
						"pressTime":0.5, #same as PRESS_TIME, but PRESS_TIME could change.
						"cooldown":1200,
						"cooldownEndTime":time.time(), #don't change this variable, this is used for logic
						"hasSound":True,
						"delayAfterSound":1,
						"soundDelayEndTime":0, #don't change this variable, this is used for logic
						"soundName":"barrelroll",
						# "sound":{
						# 	"delay":1,
						# 	"endTime":time.time(), #don't change this variable, this is used for logic
						# 	"filename":"barrelroll.mp3",
						# 	"volume":100
						# },
						"beamng":True,
						"beamCommand":"hop",
						"argument":"10",
						"hasSecondFunction":True,						
						"extraFunctions":{
							"0":{
								"beamng":True,
								"beamCommand":"DO A BARREL ROLL!",
								"argument":"-7.5",
								"endTime":100000000000, #don't change this variable, this is used for logic
								"delay":0.6
							},
							"1":{
								"beamng":True,
								"beamCommand":"DO A BARREL ROLL!",
								"argument":"5",
								"endTime":100000000000 #don't change this variable, this is used for logic
							}
						}
					},
					{
						"command":"warning",
						"waitingOnEndOfSound":False, #don't change this variable, this is used for logic
						"caseSensitive":False,
						"pressTime":PRESS_TIME,
						"cooldown":SHORT_COOLDOWN,
						"argument":"nil",
						"cooldownEndTime":time.time(), #don't change this variable, this is used for logic
						"hasSecondFunction":False,
						"hasSound":False,
						"beamng":True,
						"hasThirdFunction":False,
						"beamCommand":"warningSignal"
					},
					{
						"command":"hop",
						"waitingOnEndOfSound":False, #don't change this variable, this is used for logic
						"caseSensitive":False,
						"pressTime":PRESS_TIME,
						"cooldown":SHORT_COOLDOWN,
						"cooldownEndTime":time.time(), #don't change this variable, this is used for logic
						"hasSecondFunction":False,
						"hasSound":False,
						"beamng":True,
						"hasThirdFunction":False,
						"beamCommand":"hop",
						"argument":"3"
					},
					{
						"command":"change camera",
						"waitingOnEndOfSound":False, #don't change this variable, this is used for logic
						"caseSensitive":False,
						"pressTime":PRESS_TIME,
						"cooldown":SHORT_COOLDOWN,
						"cooldownEndTime":time.time(), #don't change this variable, this is used for logic
						"hasSecondFunction":False,
						"hasSound":False,
						"beamng":True,
						"hasThirdFunction":False,
						"beamCommand":"changeCamera",
						"argument":"nil"
					},
					{
						"command":"lights",
						"waitingOnEndOfSound":False, #don't change this variable, this is used for logic
						"caseSensitive":False,
						"pressTime":PRESS_TIME,
						"cooldown":SHORT_COOLDOWN,
						"cooldownEndTime":time.time(), #don't change this variable, this is used for logic
						"hasSecondFunction":False,
						"hasSound":False,
						"beamng":True,
						"hasThirdFunction":False,
						"beamCommand":"lights",
						"argument":"nil"
					},
					{
						"command":"you spin me right round",
						"waitingOnEndOfSound":False, #don't change this variable, this is used for logic
						"caseSensitive":False,
						"pressTime":PRESS_TIME,
						"cooldown":600,
						"cooldownEndTime":time.time(), #don't change this variable, this is used for logic
						"hasSecondFunction":False,
						"hasSound":True,
						"delayAfterSound":0.1,
						"soundDelayEndTime":0, #don't change this variable, this is used for logic
						"soundName":"spinMeRightRound",
						"beamng":True,
						"hasThirdFunction":False,
						"beamCommand":"spin",
						"argument":"10"
					},
					{
						"command":"explode",
						"waitingOnEndOfSound":False, #don't change this variable, this is used for logic
						"caseSensitive":False,
						"pressTime":PRESS_TIME,
						"cooldown":3600,
						"cooldownEndTime":time.time(), #don't change this variable, this is used for logic
						"hasSecondFunction":False,
						"hasSound":True,
						"delayAfterSound":2.5,
						"soundDelayEndTime":0, #don't change this variable, this is used for logic
						"soundName":"fbiOpenUp",
						"beamng":True,
						"hasThirdFunction":False,
						"beamCommand":"explode",
						"argument":"nil"
					},
					{
						"command":"backflip!",
						"waitingOnEndOfSound":False, #don't change this variable, this is used for logic
						"caseSensitive":False,
						"pressTime":PRESS_TIME,
						"cooldown":1800,
						"cooldownEndTime":time.time(), #don't change this variable, this is used for logic
						"hasSecondFunction":True,						
						"extraFunctions":{
								"0":{
								"beamng":True,
								"beamCommand":"backflip",
								"argument":"-4.5",
								"endTime":100000000000 #don't change this variable, this is used for logic
							}
						},
						"hasSound":True,
						"delayAfterSound":6,
						"soundDelayEndTime":0, #don't change this variable, this is used for logic
						"soundName":"backflip",
						"beamng":True,
						"hasThirdFunction":False,
						"beamCommand":"hop",
						"argument":"10"
					},
					{
						"command":"let there be light",
						"waitingOnEndOfSound":False, #don't change this variable, this is used for logic
						"caseSensitive":False,
						"pressTime":1,
						"cooldown":1800,
						"cooldownEndTime":time.time(), #don't change this variable, this is used for logic
						"hasSecondFunction":True,						
						"extraFunctions":{
							"0":{
								"beamng":True,
								"beamCommand":"screenRGB",
								"argument":"86 86 86",
								"endTime":100000000000, #don't change this variable, this is used for logic
								"delay": 0.5
							},
							"1":{
								"beamng":True,
								"beamCommand":"screenRGB",
								"argument":"64 64 64",
								"endTime":100000000000, #don't change this variable, this is used for logic
								"delay": 0.5
							},
							"2":{
								"beamng":True,
								"beamCommand":"stopScreenRGB",
								"argument":"0 0 0",
								"endTime":100000000000, #don't change this variable, this is used for logic
								"delay": 0.1
							}
						},
						"hasSound":True,
						"delayAfterSound":2,
						"soundDelayEndTime":0, #don't change this variable, this is used for logic
						"soundName":"Flashbang",
						"beamng":True,
						"hasThirdFunction":False,
						"beamCommand":"screenRGB",
						"argument":"128 128 128"
					},
					{
						"command":"MOVE IT MOVE IT!", 
						"waitingOnEndOfSound":False, #don't change this variable, this is used for logic
						"caseSensitive":True,
						"pressTime":0.3, 
						"cooldown":1200,
						"cooldownEndTime":time.time(), #don't change this variable, this is used for logic
						"hasSound":True,
						"delayAfterSound":0,
						"soundDelayEndTime":0, #don't change this variable, this is used for logic
						"soundName":"moveit",
						# "sound":{
						# 	"delay":1,
						# 	"endTime":time.time(), #don't change this variable, this is used for logic
						# 	"filename":"barrelroll.mp3",
						# 	"volume":100
						# },
						"beamng":True,
						"beamCommand":"spin",
						"argument":"2",
						"hasSecondFunction":True,						
						"extraFunctions":{
							"0":{
								"beamng":True,
								"beamCommand":"spin",
								"argument":"-2",
								"endTime":100000000000, #don't change this variable, this is used for logic
								"delay":0.01
							},
							"1":{
								"beamng":True,
								"beamCommand":"spin",
								"argument":"-2",
								"endTime":100000000000, #don't change this variable, this is used for logic
								"delay":0.3
							},
							"2":{
								"beamng":True,
								"beamCommand":"spin",
								"argument":"2",
								"endTime":100000000000, #don't change this variable, this is used for logic
								"delay":0.01
							},
							"3":{
								"beamng":True,
								"beamCommand":"spin",
								"argument":"2",
								"endTime":100000000000, #don't change this variable, this is used for logic
								"delay":0.3
							},
							"4":{
								"beamng":True,
								"beamCommand":"spin",
								"argument":"-2",
								"endTime":100000000000, #don't change this variable, this is used for logic
								"delay":0.01
							},
							"5":{
								"beamng":True,
								"beamCommand":"spin",
								"argument":"-2",
								"endTime":100000000000, #don't change this variable, this is used for logic
								"delay":0.3
							},
							"6":{
								"beamng":True,
								"beamCommand":"spin",
								"argument":"2",
								"endTime":100000000000, #don't change this variable, this is used for logic
								"delay":0.01
							},
							"7":{
								"beamng":True,
								"beamCommand":"spin",
								"argument":"2",
								"endTime":100000000000, #don't change this variable, this is used for logic
								"delay":0.3
							},
							"8":{
								"beamng":True,
								"beamCommand":"spin",
								"argument":"-2",
								"endTime":100000000000, #don't change this variable, this is used for logic
								"delay":0.01
							},
							"9":{
								"beamng":True,
								"beamCommand":"spin",
								"argument":"-2",
								"endTime":100000000000, #don't change this variable, this is used for logic
								"delay":0.3
							},
							"10":{
								"beamng":True,
								"beamCommand":"spin",
								"argument":"2",
								"endTime":100000000000, #don't change this variable, this is used for logic
								"delay":0.01
							}
						}
					},
					{
						"command":"DJ OTTO!", 
						"waitingOnEndOfSound":False, #don't change this variable, this is used for logic
						"caseSensitive":True,
						"pressTime":0.3, 
						"cooldown":600,
						"cooldownEndTime":time.time(), #don't change this variable, this is used for logic
						"hasSound":True,
						"delayAfterSound":0,
						"soundDelayEndTime":0, #don't change this variable, this is used for logic
						"soundName":"Otto",
						# "sound":{
						# 	"delay":1,
						# 	"endTime":time.time(), #don't change this variable, this is used for logic
						# 	"filename":"barrelroll.mp3",
						# 	"volume":100
						# },
						"beamng":True,
						"beamCommand":"screenRGB",
						"argument":"0.5 0 0",
						"hasSecondFunction":True,						
						"extraFunctions":{
							"0":{
								"beamng":True,
								"beamCommand":"screenRGB",
								"argument":"0 0.5 0",
								"endTime":100000000000, #don't change this variable, this is used for logic
								"delay":0.3
							},
							"1":{
								"beamng":True,
								"beamCommand":"screenRGB",
								"argument":"0 0 0.5",
								"endTime":100000000000, #don't change this variable, this is used for logic
								"delay":0.3
							},
							"2":{
								"beamng":True,
								"beamCommand":"screenRGB",
								"argument":"0.5 0.5 0",
								"endTime":100000000000, #don't change this variable, this is used for logic
								"delay":0.3
							},
							"3":{
								"beamng":True,
								"beamCommand":"screenRGB",
								"argument":"0 0.5 0.5",
								"endTime":100000000000, #don't change this variable, this is used for logic
								"delay":0.3
							},
							"4":{
								"beamng":True,
								"beamCommand":"screenRGB",
								"argument":"0.5 0 0",
								"endTime":100000000000, #don't change this variable, this is used for logic
								"delay":0.3
							},
							"5":{
								"beamng":True,
								"beamCommand":"screenRGB",
								"argument":"0 0.5 0",
								"endTime":100000000000, #don't change this variable, this is used for logic
								"delay":0.3
							},
							"6":{
								"beamng":True,
								"beamCommand":"screenRGB",
								"argument":"0 0 0.5",
								"endTime":100000000000, #don't change this variable, this is used for logic
								"delay":0.3
							},
							"7":{
								"beamng":True,
								"beamCommand":"screenRGB",
								"argument":"0.5 0.5 0",
								"endTime":100000000000, #don't change this variable, this is used for logic
								"delay":0.3
							},
							"8":{
								"beamng":True,
								"beamCommand":"screenRGB",
								"argument":"0 0.5 0.5",
								"endTime":100000000000, #don't change this variable, this is used for logic
								"delay":0.3
							},
							"9":{
								"beamng":True,
								"beamCommand":"screenRGB",
								"argument":"0.5 0 0",
								"endTime":100000000000, #don't change this variable, this is used for logic
								"delay":0.3
							},
							"10":{
								"beamng":True,
								"beamCommand":"screenRGB",
								"argument":"0 0.5 0",
								"endTime":100000000000, #don't change this variable, this is used for logic
								"delay":0.3
							},
							"11":{
								"beamng":True,
								"beamCommand":"screenRGB",
								"argument":"0 0 0.5",
								"endTime":100000000000, #don't change this variable, this is used for logic
								"delay":0.3
							},
							"12":{
								"beamng":True,
								"beamCommand":"screenRGB",
								"argument":"0.5 0.5 0",
								"endTime":100000000000, #don't change this variable, this is used for logic
								"delay":0.3
							},
							"13":{
								"beamng":True,
								"beamCommand":"screenRGB",
								"argument":"0 0.5 0.5",
								"endTime":100000000000, #don't change this variable, this is used for logic
								"delay":0.3
							},
							"14":{
								"beamng":True,
								"beamCommand":"screenRGB",
								"argument":"0.5 0 0",
								"endTime":100000000000, #don't change this variable, this is used for logic
								"delay":0.3
							},
							"15":{
								"beamng":True,
								"beamCommand":"screenRGB",
								"argument":"0 0.5 0",
								"endTime":100000000000, #don't change this variable, this is used for logic
								"delay":0.3
							},
							"16":{
								"beamng":True,
								"beamCommand":"screenRGB",
								"argument":"0 0 0.5",
								"endTime":100000000000, #don't change this variable, this is used for logic
								"delay":0.3
							},
							"17":{
								"beamng":True,
								"beamCommand":"screenRGB",
								"argument":"0.5 0.5 0",
								"endTime":100000000000, #don't change this variable, this is used for logic
								"delay":0.3
							},
							"18":{
								"beamng":True,
								"beamCommand":"screenRGB",
								"argument":"0 0.5 0.5",
								"endTime":100000000000, #don't change this variable, this is used for logic
								"delay":0.3
							},
							"19":{
								"beamng":True,
								"beamCommand":"screenRGB",
								"argument":"0.5 0 0.5",
								"endTime":100000000000, #don't change this variable, this is used for logic
								"delay":0.3
							},
							"20":{
								"beamng":True,
								"beamCommand":"screenRGB",
								"argument":"0.5 0 0",
								"endTime":100000000000, #don't change this variable, this is used for logic
								"delay":0.3
							},
							"21":{
								"beamng":True,
								"beamCommand":"screenRGB",
								"argument":"0 0.5 0",
								"endTime":100000000000, #don't change this variable, this is used for logic
								"delay":0.3
							},
							"22":{
								"beamng":True,
								"beamCommand":"screenRGB",
								"argument":"0 0 0.5",
								"endTime":100000000000, #don't change this variable, this is used for logic
								"delay":0.3
							},
							"23":{
								"beamng":True,
								"beamCommand":"screenRGB",
								"argument":"0.5 0.5 0",
								"endTime":100000000000, #don't change this variable, this is used for logic
								"delay":0.3
							},
							"24":{
								"beamng":True,
								"beamCommand":"screenRGB",
								"argument":"0 0.5 0.5",
								"endTime":100000000000, #don't change this variable, this is used for logic
								"delay":0.3
							},
							"25":{
								"beamng":True,
								"beamCommand":"screenRGB",
								"argument":"0.5 0 0.5",
								"endTime":100000000000, #don't change this variable, this is used for logic
								"delay":0.3
							},
							"26":{
								"beamng":True,
								"beamCommand":"screenRGB",
								"argument":"0.5 0 0",
								"endTime":100000000000, #don't change this variable, this is used for logic
								"delay":0.3
							},
							"27":{
								"beamng":True,
								"beamCommand":"screenRGB",
								"argument":"0 0.5 0",
								"endTime":100000000000, #don't change this variable, this is used for logic
								"delay":0.3
							},
							"28":{
								"beamng":True,
								"beamCommand":"screenRGB",
								"argument":"0 0 0.5",
								"endTime":100000000000, #don't change this variable, this is used for logic
								"delay":0.3
							},
							"29":{
								"beamng":True,
								"beamCommand":"screenRGB",
								"argument":"0.5 0.5 0",
								"endTime":100000000000, #don't change this variable, this is used for logic
								"delay":0.3
							},
							"30":{
								"beamng":True,
								"beamCommand":"screenRGB",
								"argument":"0 0.5 0.5",
								"endTime":100000000000, #don't change this variable, this is used for logic
								"delay":0.3
							},
							"31":{
								"beamng":True,
								"beamCommand":"screenRGB",
								"argument":"0 0.5 0",
								"endTime":100000000000, #don't change this variable, this is used for logic
								"delay":0.3
							},
							"32":{
								"beamng":True,
								"beamCommand":"screenRGB",
								"argument":"0 0 0.5",
								"endTime":100000000000, #don't change this variable, this is used for logic
								"delay":0.3
							},
							"33":{
								"beamng":True,
								"beamCommand":"screenRGB",
								"argument":"0.5 0.5 0",
								"endTime":100000000000, #don't change this variable, this is used for logic
								"delay":0.3
							},
							"34":{
								"beamng":True,
								"beamCommand":"screenRGB",
								"argument":"0 0.5 0.5",
								"endTime":100000000000, #don't change this variable, this is used for logic
								"delay":0.3
							},
							"35":{
								"beamng":True,
								"beamCommand":"screenRGB",
								"argument":"0.5 0 0.5",
								"endTime":100000000000, #don't change this variable, this is used for logic
								"delay":0.3
							},
							"36":{
								"beamng":True,
								"beamCommand":"screenRGB",
								"argument":"0.5 0 0",
								"endTime":100000000000, #don't change this variable, this is used for logic
								"delay":0.3
							},
							"37":{
								"beamng":True,
								"beamCommand":"screenRGB",
								"argument":"0 0.5 0",
								"endTime":100000000000, #don't change this variable, this is used for logic
								"delay":0.3
							},
							"38":{
								"beamng":True,
								"beamCommand":"screenRGB",
								"argument":"0 0 0.5",
								"endTime":100000000000, #don't change this variable, this is used for logic
								"delay":0.3
							},
							"39":{
								"beamng":True,
								"beamCommand":"screenRGB",
								"argument":"0.5 0.5 0",
								"endTime":100000000000, #don't change this variable, this is used for logic
								"delay":0.3
							},
							"40":{
								"beamng":True,
								"beamCommand":"screenRGB",
								"argument":"0.5 0 0.5",
								"endTime":100000000000, #don't change this variable, this is used for logic
								"delay":0.3
							},
							"41":{
								"beamng":True,
								"beamCommand":"screenRGB",
								"argument":"0.5 0 0",
								"endTime":100000000000, #don't change this variable, this is used for logic
								"delay":0.3
							},
							"42":{
								"beamng":True,
								"beamCommand":"stopScreenRGB",
								"argument":"0 0 0",
								"endTime":100000000000, #don't change this variable, this is used for logic
								"delay":0.3
							}
						}
					},
					{
						"command":"where is the zaza?", 
						"waitingOnEndOfSound":False, #don't change this variable, this is used for logic
						"caseSensitive":False,
						"pressTime":0.1, 
						"cooldown":600,
						"cooldownEndTime":time.time(), #don't change this variable, this is used for logic
						"hasSound":True,
						"delayAfterSound":0.1,
						"soundDelayEndTime":0, #don't change this variable, this is used for logic
						"soundName":"snoopdogg",
						"beamCommand":"switchUILayout",
						"argument":"svc",
						"beamng":True,
						"hasSecondFunction":True,						
						"extraFunctions":{
							"0":{
								"beamng":True,
								"beamCommand":"FullscreenImage",
								"argument":"Smog.gif",
								"endTime":100000000000, #don't change this variable, this is used for logic
								"delay":0.1
							},
							"1":{
								"beamng":True,
								"beamCommand":"DVDImage",
								"argument":"SnoopDogg.gif",
								"endTime":100000000000, #don't change this variable, this is used for logic
								"delay":0.1
							},
							"2":{
								"beamng":True,
								"beamCommand":"screenRGB",
								"argument":"0 10 0",
								"endTime":100000000000, #don't change this variable, this is used for logic
								"delay":12
							},
							"3":{
								"beamng":True,
								"beamCommand":"stopScreenRGB",
								"argument":"0 0 0",
								"endTime":100000000000, #don't change this variable, this is used for logic
								"delay":0.1
							},
							"4":{
								"beamng":True,
								"beamCommand":"stopDVDImage",
								"argument":"SnoopDogg.gif",
								"endTime":100000000000, #don't change this variable, this is used for logic
								"delay":0.1
							},
							"5":{
								"beamng":True,
								"beamCommand":"stopFullscreenImage",
								"argument":"Smog.gif",
								"endTime":100000000000, #don't change this variable, this is used for logic
								"delay":0.1
							},
							"6":{
								"beamng":True,
								"beamCommand":"switchUILayout",
								"argument":"multiplayer",
								"endTime":100000000000, #don't change this variable, this is used for logic
								"delay":0.1
							}
						}
					} # ,
					# {
					# 	"command":"banana", 
					# 	"waitingOnEndOfSound":False, #don't change this variable, this is used for logic
					# 	"caseSensitive":False,
					# 	"pressTime":0.2, #same as PRESS_TIME, but that could change.
					# 	"cooldown":600,
					# 	"cooldownEndTime":time.time(), #don't change this variable, this is used for logic
					# 	"hasSound":False,
					# 	"beamng":True,
					# 	"beamCommand":"ice",
					# 	"argument":"10",
					# 	"hasSecondFunction":True,
					# 	"secondFunction":{
					# 		"beamng":True,
					# 		"beamCommand":"spin",
					# 		"argument":"15",
					# 		"endTime":100000000000, #don't change this variable, this is used for logic
					# 		"delay":0.6
					# 	},
					# 	"hasThirdFunction":True,
					# 	"thirdFunction":{
					# 		"beamng":True,
					# 		"beamCommand":"stopIce",
					# 		"argument":"5",
					# 		"endTime":100000000000 #don't change this variable, this is used for logic
					# 	}
					# }
				]

message = ""
user = ""


def gamecontrol():
	global message
	global beammp_name
	beammp_name = "-1" #-1 for all players
	# ignitionEndTime = 100000000000
	emptyBuffer = {
		"name": "",
		"message": "",
		"argument": ""
	}
	sendToBeamNG(emptyBuffer) #create the data file
	printPinMessage()
	# ALL_COMMANDS_DELAY = 30 #s
	# ALL_COMMANDS_DELAY_ENDTIME = 0
	targeting_prefix = "Target "
	while True:
		if message.startswith(targeting_prefix): 
			beammp_name = message[len(targeting_prefix):]
			message = ""
			# print(beammp_name)
		commandsOnChat()
		extraCommands()

def printPinMessage():
	print("\n\n\n\n\n\n\n")
	print("/pin Chat commands (commands with capital letters are case sensitive): ")
	for data in BEAMNGCOMMANDS:
		print(data["command"] + ", ")
	print("\n\n\n\n\n\n\n")

def handleSound(commandData):
	buffer = {
		"name": beammp_name,
		"message": "playSound",
		"argument": commandData["soundName"]
	}
	sendToBeamNG(buffer)
	commandData["soundDelayEndTime"] = time.time() + commandData["delayAfterSound"]
	return commandData

def commandsOnChat():
	global message
	for data in BEAMNGCOMMANDS:
		if (not data["caseSensitive"] and data["command"] == message.lower()) or (data["caseSensitive"] and data["command"] == message) or data["waitingOnEndOfSound"]:
			if data["cooldown"]:
				if time.time() < data["cooldownEndTime"]:
					message = "" #this command is still on cooldown
					continue
			if data["beamng"]:
				if data["hasSound"]:
					if data["soundDelayEndTime"] == 0:
						data["waitingOnEndOfSound"] = True
						handleSound(data)
				if data["hasSound"]:
					if time.time() < data["soundDelayEndTime"]:
						continue
					else:
						data["waitingOnEndOfSound"] = False
						data["soundDelayEndTime"] = 0
				buffer = {
					"name": beammp_name,
					"message": data["beamCommand"],
					"argument": data["argument"]
				}
				sendToBeamNG(buffer)
				if "extraFunctions" in data.keys():
					data["extraFunctions"]["0"]["endTime"] = time.time() + data["pressTime"]
				if data["cooldown"]:
					data["cooldownEndTime"] = time.time() + data["cooldown"]
				# if data["hasSound"]: #kept here for when someone wants a sound effect for the streamer alone
				# 	data["sound"]["endTime"] = time.time() + data["sound"]["delay"]
			message = ""

def extraCommands(): #this should be a table in the datastructure...
	global message
	for data in BEAMNGCOMMANDS:
		if "extraFunctions" in data.keys():
			# print(data["extraFunctions"])
			for i in data["extraFunctions"]:
				if time.time() > data["extraFunctions"][i]["endTime"]:
					buffer = {
						"name": beammp_name,
						"message": data["extraFunctions"][i]["beamCommand"],
						"argument": data["extraFunctions"][i]["argument"]
					}
					sendToBeamNG(buffer)
					data["extraFunctions"][i]["endTime"] = 100000000000
					if str(int(i) + 1) in data["extraFunctions"]:
						data["extraFunctions"][str(int(i) + 1)]["endTime"] = time.time() + data["extraFunctions"][i]["delay"]
			
# def secondCommandsAfterDelay(): #this should be a table in the datastructure...
# 	global message
# 	for data in BEAMNGCOMMANDS:
# 		# if data["hasSound"] and time.time() > data["sound"]["endTime"]:
# 		# 	continue
# 		if data["hasSecondFunction"] and time.time() > data["secondFunction"]["endTime"]:
# 			buffer = {
# 				"name": beammp_name,
# 				"message": data["secondFunction"]["beamCommand"],
# 				"argument": data["secondFunction"]["argument"]
# 			}
# 			sendToBeamNG(buffer)
# 			data["secondFunction"]["endTime"] = 100000000000
# 			if data["hasThirdFunction"]:
# 				data["thirdFunction"]["endTime"] = time.time() + data["secondFunction"]["delay"]
			
# def thirdCommandsAfterDelay():
# 	global message
# 	for data in BEAMNGCOMMANDS:
# 		if data["hasThirdFunction"] and time.time() > data["thirdFunction"]["endTime"]:
# 			buffer = {
# 				"name": beammp_name,
# 				"message": data["thirdFunction"]["beamCommand"],
# 				"argument": data["thirdFunction"]["argument"]
# 			}
# 			sendToBeamNG(buffer)
# 			data["thirdFunction"]["endTime"] = 100000000000

def sendToBeamNG(buffer):
	existing_data = []  # Initialize with an empty list

	# Check if the file exists and is not empty
	if os.path.isfile(BEAMMP_SERVER_EXE_FOLDER + "/StreamersVsChatData.json") and os.path.getsize(BEAMMP_SERVER_EXE_FOLDER + "/StreamersVsChatData.json") > 0:
		with open(BEAMMP_SERVER_EXE_FOLDER + "/StreamersVsChatData.json", "rb") as file:
			if file.read(2) != '[]' and file.read(2) != '{}': #https://stackoverflow.com/questions/47792142/how-to-check-if-json-file-contains-only-empty-array
				file.seek(0)  # it may be redundant but it does not hurt
				existing_data = json.load(file)
			# Append the new data to the existing data
	existing_data.append(buffer)
	with open(BEAMMP_SERVER_EXE_FOLDER + "/StreamersVsChatData.json", "w") as file:
		json.dump(existing_data, file)
		file.close()

# def playSound(file, volume = 100):
# 	soundsPath = "C:\\Users\\Julian\\Documents\\dev\\TwitchPlays\\Sounds\\"
# 	p = vlc.MediaPlayer("file:///" + soundsPath + file)
# 	p.audio_set_delay(100)
# 	p.audio_set_volume(volume)
# 	p.play()
	

def twitch():

	global user
	global message

	def joinchat():
		Loading = True
		while Loading:
			readbuffer_join = irc.recv(1024)
			readbuffer_join = readbuffer_join.decode()
			print(readbuffer_join)
			for line in readbuffer_join.split("\n")[0:-1]:
				print(line)
				Loading = loadingComplete(line)

	def loadingComplete(line):
		if("End of /NAMES list" in line):
			print("TwitchBot has joined " + CHANNEL + "'s Channel!")
			sendMessage(irc, "Twitch can now control inputs!")
			return False
		else:
			return True

	def sendMessage(irc, message):
		messageTemp = "PRIVMSG #" + CHANNEL + " :" + message
		irc.send((messageTemp + "\n").encode())

	def getUser(line):
		#global user
		colons = line.count(":")
		colonless = colons-1
		separate = line.split(":", colons)
		user = separate[colonless].split("!", 1)[0]
		return user

	def getMessage(line):
		#global message
		try:
			colons = line.count(":")
			message = (line.split(":", colons))[colons]
		except:
			message = ""
		return message

	def console(line):
		if "PRIVMSG" in line:
			return False
		else:
			return True

	joinchat()
	irc.send("CAP REQ :twitch.tv/tags\r\n".encode())
	while True:
		try:
			readbuffer = irc.recv(1024).decode()
		except:
			readbuffer = ""
		for line in readbuffer.split("\r\n"):
			if line == "":
				continue
			if "PING :tmi.twitch.tv" in line:
				print(line)
				msgg = "PONG :tmi.twitch.tv\r\n".encode()
				irc.send(msgg)
				print(msgg)
				continue
			else:
				try:
					user = getUser(line)
					message = getMessage(line)
					print(user + " : " + message)
				except Exception:
					pass

def main():
	if __name__ =='__main__':
		t1 = threading.Thread(target = twitch)
		t1.start()
		t2 = threading.Thread(target = gamecontrol)
		t2.start()
main()