import socket
import threading
from ahk import AHK #auto hotkey
import time
import json #to write data file
import os #check file size
import vlc #sound effects

#Download Autohotkey at https://www.autohotkey.com/ and provide the address to
#AutoHotkey.exe below!
ahk = AHK(executable_path='C:\\Program Files\\AutoHotkey\\v2\\AutoHotkey.exe')

SERVER = "irc.twitch.tv"
PORT = 6667

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

BEAMMP_NAME = "-1" #-1 for all players


PRESS_TIME = 0.5 #s
SHORT_COOLDOWN = 1 #s

BEAMNGCOMMANDS = [
					{	#use honk as an example for a command which triggers two commands and has no sound effect
						"command":"honk",
						"caseSensitive":False,
						"pressTime":PRESS_TIME,
						"cooldown":SHORT_COOLDOWN,
						"cooldownEndTime":time.time(),
						"hasSecondFunction":True,
						"hasSound":False,
						"beamng":True,
						"hasThirdFunction":False,
						"beamCommand":"honk",
						"argument":"nil",
						"secondFunction":{"beamng":True,
							"beamCommand":"stopHonk",
							"argument":"nil",
							"endTime":100000000000
						}
					},
					{	#use siren as an example for a command which triggers one command and has no sound effect
						"command":"siren",
						"caseSensitive":False,
						"pressTime":PRESS_TIME,
						"cooldown":SHORT_COOLDOWN,
						"argument":"nil",
						"cooldownEndTime":time.time(),
						"hasSecondFunction":False,
						"hasSound":False,
						"beamng":True,
						"hasThirdFunction":False,
						"beamCommand":"siren"
					},
					{	
						"command":"brake",
						"caseSensitive":False,
						"pressTime":PRESS_TIME,
						"cooldown":SHORT_COOLDOWN,
						"cooldownEndTime":time.time(),
						"hasSecondFunction":True,
						"hasSound":False,
						"beamng":True,
						"hasThirdFunction":False,
						"beamCommand":"brake",
						"argument":"nil",
						"secondFunction":
						{
							"beamng":True,
							"beamCommand":"stopBrake",
							"argument":"nil",
							"endTime":100000000000
						}
					},
					{	
						"command":"gas",
						"caseSensitive":False,
						"pressTime":PRESS_TIME,
						"cooldown":SHORT_COOLDOWN,
						"cooldownEndTime":time.time(),
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
							"endTime":100000000000
						}
					},
					{
						"command":"And his name is... JOHN CENA!!!",
						"caseSensitive":True,
						"pressTime":1,
						"cooldown":1800, #30 minutes
						"cooldownEndTime":time.time(),
						"hasSecondFunction":True,
						"hasSound":True,
						"delayAfterSound":0.1,
						"soundDelayEndTime":0,
						"soundName":"JOHNCENA",
						# "sound":{ #sound effects are now done in beamng, so that everyone hears them
						# 	"delay":0,
						# 	"endTime":time.time(),
						# 	"filename":"JOHNCENA.mp3",
						# 	"volume":80
						# },
						"beamng":True,
						"hasThirdFunction":True,
						"beamCommand":"johncena",
						"argument":"nil",
						"secondFunction":{
							"beamng":True,
							"beamCommand":"hop",
							"argument":"20",
							"delay":1,
							"endTime":100000000000
						},
						"thirdFunction":{
							"beamng":True,
							"beamCommand":"hop",
							"argument":"-40",
							"endTime":100000000000
						}
					},
					{
						"command":"boost",
						"caseSensitive":False,
						"pressTime":PRESS_TIME,
						"cooldown":SHORT_COOLDOWN,
						"cooldownEndTime":time.time(),
						"hasSecondFunction":False,
						# "hasSound":False, #implemented in VE lua
						"beamng":True,
						"hasThirdFunction":False,
						# "sound":{
						# 	"delay":0,
						# 	"endTime":time.time(),
						# 	"filename":"GASGASGAS.mp3",
						# 	"volume":80
						# },
						"hasSound":True,
						"delayAfterSound":0.1,
						"soundDelayEndTime":0,
						"soundName":"GASGASGAS",
						"beamCommand":"boost",
						"argument":"10"
					},
					{
						"command":"boost backwards",
						"caseSensitive":False,
						"pressTime":PRESS_TIME,
						"cooldown":SHORT_COOLDOWN,
						"cooldownEndTime":time.time(),
						"hasSecondFunction":False,
						"hasSound":False,
						"beamng":True,
						"hasThirdFunction":False,
						"beamCommand":"boost",
						"argument":"-4"
					},
					{	
						"command":"handbrake",
						"caseSensitive":False,
						"pressTime":PRESS_TIME,
						"cooldown":SHORT_COOLDOWN,
						"cooldownEndTime":time.time(),
						"hasSecondFunction":True,
						"hasSound":False,
						"beamng":True,
						"hasThirdFunction":False,
						"beamCommand":"handbrake",
						"argument":"nil",
						"secondFunction":{
							"beamng":True,
							"beamCommand":"stopHandbrake",
							"argument":"nil",
							"endTime":100000000000
						}
					},
					{
						"command":"i'm blind",
						"caseSensitive":False,
						"pressTime":3, #sound effect is 3 seconds long
						"cooldown":600,
						"cooldownEndTime":time.time(),
						"hasSecondFunction":True,
						# "hasSound":False, #implemented in VE lua
						"beamng":True,
						"hasThirdFunction":False,
						# "sound":{
						# 	"delay":0,
						# 	"endTime":time.time(),
						# 	"filename":"blind.mp3",
						# 	"volume":100
						# },
						"hasSound":True,
						"delayAfterSound":1,
						"soundDelayEndTime":0,
						"soundName":"blind",
						"beamCommand":"blind",
						"argument":"nil",
						"secondFunction":{
							"beamng":True,
							"beamCommand":"stopBlind",
							"argument":"nil",
							"endTime":100000000000
						}
					},
					{
						"command":"look back",
						"caseSensitive":False,
						"pressTime":PRESS_TIME,
						"cooldown":SHORT_COOLDOWN,
						"cooldownEndTime":time.time(),
						"hasSecondFunction":True,
						"hasSound":False,
						"beamng":True,
						"hasThirdFunction":False,
						"beamCommand":"lookBack",
						"argument":"nil",
						"secondFunction":{
							"beamng":True,
							"beamCommand":"stopLookBack",
							"argument":"nil",
							"endTime":100000000000
						}
					},
					{
						"command":"moon",
						"caseSensitive":False,
						"pressTime":1,
						"cooldown":SHORT_COOLDOWN,
						"cooldownEndTime":time.time(),
						"hasSecondFunction":True,
						"hasSound":False,
						"beamng":True,
						"hasThirdFunction":False,
						"beamCommand":"moon",
						"argument":"nil",
						"secondFunction":{
							"beamng":True,
							"beamCommand":"earth",
							"argument":"nil",
							"endTime":100000000000
						}
					},
					{
						"command":"clutch",
						"caseSensitive":False,
						"pressTime":PRESS_TIME,
						"cooldown":SHORT_COOLDOWN,
						"cooldownEndTime":time.time(),
						"hasSecondFunction":True,
						"hasSound":False,
						"beamng":True,
						"hasThirdFunction":False,
						"beamCommand":"clutch",
						"argument":"nil",
						"secondFunction":{
							"beamng":True,
							"beamCommand":"stopClutch",
							"argument":"nil",
							"endTime":100000000000
						}
					},
					{
						"command":"drift",
						"caseSensitive":False,
						"pressTime":PRESS_TIME,
						"cooldown":SHORT_COOLDOWN,
						"cooldownEndTime":time.time(),
						"hasSecondFunction":True,
						# "hasSound":False, #implemented in VE lua
						# "sound":{
						# 	"delay":0,
						# 	"endTime":time.time(),
						# 	"filename":"tokyo.mp3",
						# 	"volume":100
						# },
						"hasSound":True,
						"delayAfterSound":0.1,
						"soundDelayEndTime":0,
						"soundName":"tokyo",
						"beamng":True,
						"hasThirdFunction":False,
						"beamCommand":"drift",
						"argument":"nil",
						"secondFunction":{
							"beamng":True,
							"beamCommand":"stopDrift",
							"argument":"nil",
							"endTime":100000000000
						}
					},
					{
						"command":"look left",
						"caseSensitive":False,
						"pressTime":PRESS_TIME,
						"cooldown":SHORT_COOLDOWN,
						"cooldownEndTime":time.time(),
						"hasSecondFunction":True,
						"hasSound":False,
						"beamng":True,
						"hasThirdFunction":False,
						"beamCommand":"lookLeft",
						"argument":"nil",
						"secondFunction":{
							"beamng":True,
							"beamCommand":"stopLookLeft",
							"argument":"nil",
							"endTime":100000000000
						}
					},
					{
						"command":"look right",
						"caseSensitive":False,
						"pressTime":PRESS_TIME,
						"cooldown":SHORT_COOLDOWN,
						"cooldownEndTime":time.time(),
						"hasSecondFunction":True,
						"hasSound":False,
						"beamng":True,
						"hasThirdFunction":False,
						"beamCommand":"lookRight",
						"argument":"nil",
						"secondFunction":{
							"beamng":True,
							"beamCommand":"stopLookRight",
							"argument":"nil",
							"endTime":100000000000
						}
					},
					{
						"command":"right",
						"caseSensitive":False,
						"pressTime":PRESS_TIME,
						"cooldown":SHORT_COOLDOWN,
						"cooldownEndTime":time.time(),
						"hasSecondFunction":True,
						"hasSound":False,
						"beamng":True,
						"hasThirdFunction":False,
						"beamCommand":"steerRight",
						"argument":"nil",
						"secondFunction":{
							"beamng":True,
							"beamCommand":"stopSteerRight",
							"argument":"nil",
							"endTime":100000000000
						}
					},
					{
						"command":"left",
						"caseSensitive":False,
						"pressTime":PRESS_TIME,
						"cooldown":SHORT_COOLDOWN,
						"cooldownEndTime":time.time(),
						"hasSecondFunction":True,
						"hasSound":False,
						"beamng":True,
						"hasThirdFunction":False,
						"beamCommand":"steerLeft",
						"argument":"nil",
						"secondFunction":{
							"beamng":True,
							"beamCommand":"stopSteerLeft",
							"argument":"nil",
							"endTime":100000000000
						}
					},
					{
						"command":"ice ice baby",
						"caseSensitive":False,
						"pressTime":PRESS_TIME,
						"cooldown":SHORT_COOLDOWN,
						"cooldownEndTime":time.time(),
						"hasSecondFunction":True,
						"hasSound":True,
						"delayAfterSound":1,
						"soundDelayEndTime":0,
						"soundName":"iceIceBaby",
						"beamng":True,
						"hasThirdFunction":False,
						"beamCommand":"ice",
						"argument":"nil",
						"secondFunction":{
							"beamng":True,
							"beamCommand":"stopIce",
							"argument":"nil",
							"endTime":100000000000
						}
					},
					{
						"command":"DO A BARREL ROLL!", #TODO: figure out a better way to do multiple functions on one command
						"caseSensitive":True,
						"pressTime":0.5, #same as PRESS_TIME, but that could change.
						"cooldown":1200,
						"cooldownEndTime":time.time(),
						"hasSound":True,
						"delayAfterSound":1,
						"soundDelayEndTime":0,
						"soundName":"barrelroll",
						# "sound":{
						# 	"delay":1,
						# 	"endTime":time.time(),
						# 	"filename":"barrelroll.mp3",
						# 	"volume":100
						# },
						"beamng":True,
						"beamCommand":"hop",
						"argument":"10",
						"hasSecondFunction":True,
						"secondFunction":{
							"beamng":True,
							"beamCommand":"DO A BARREL ROLL!",
							"argument":"-7.5",
							"endTime":100000000000,
							"delay":0.6
						},
						"hasThirdFunction":True,
						"thirdFunction":{
							"beamng":True,
							"beamCommand":"DO A BARREL ROLL!",
							"argument":"5",
							"endTime":100000000000
						}
					},
					{
						"command":"warning",
						"caseSensitive":False,
						"pressTime":PRESS_TIME,
						"cooldown":SHORT_COOLDOWN,
						"argument":"nil",
						"cooldownEndTime":time.time(),
						"hasSecondFunction":False,
						"hasSound":False,
						"beamng":True,
						"hasThirdFunction":False,
						"beamCommand":"warningSignal"
					},
					{
						"command":"hop",
						"caseSensitive":False,
						"pressTime":PRESS_TIME,
						"cooldown":SHORT_COOLDOWN,
						"cooldownEndTime":time.time(),
						"hasSecondFunction":False,
						"hasSound":False,
						"beamng":True,
						"hasThirdFunction":False,
						"beamCommand":"hop",
						"argument":"3"
					},
					{
						"command":"change camera",
						"caseSensitive":False,
						"pressTime":PRESS_TIME,
						"cooldown":SHORT_COOLDOWN,
						"cooldownEndTime":time.time(),
						"hasSecondFunction":False,
						"hasSound":False,
						"beamng":True,
						"hasThirdFunction":False,
						"beamCommand":"changeCamera",
						"argument":"nil"
					},
					{
						"command":"lights",
						"caseSensitive":False,
						"pressTime":PRESS_TIME,
						"cooldown":SHORT_COOLDOWN,
						"cooldownEndTime":time.time(),
						"hasSecondFunction":False,
						"hasSound":False,
						"beamng":True,
						"hasThirdFunction":False,
						"beamCommand":"lights",
						"argument":"nil"
					},
					{
						"command":"you spin me right round",
						"caseSensitive":False,
						"pressTime":PRESS_TIME,
						"cooldown":600,
						"cooldownEndTime":time.time(),
						"hasSecondFunction":False,
						"hasSound":True,
						"delayAfterSound":0.1,
						"soundDelayEndTime":0,
						"soundName":"spinMeRightRound",
						"beamng":True,
						"hasThirdFunction":False,
						"beamCommand":"spin",
						"argument":"15"
					},
					{
						"command":"explode",
						"caseSensitive":False,
						"pressTime":PRESS_TIME,
						"cooldown":3600,
						"cooldownEndTime":time.time(),
						"hasSecondFunction":False,
						"hasSound":True,
						"delayAfterSound":2.5,
						"soundDelayEndTime":0,
						"soundName":"fbiOpenUp",
						"beamng":True,
						"hasThirdFunction":False,
						"beamCommand":"explode",
						"argument":"nil"
					},
					{
						"command":"backflip!",
						"caseSensitive":False,
						"pressTime":PRESS_TIME,
						# "cooldown":1800,
						"cooldown":0,
						"cooldownEndTime":time.time(),
						"hasSecondFunction":True,
						"secondFunction":{
							"beamng":True,
							"beamCommand":"backflip",
							"argument":"-4.5",
							"endTime":100000000000
						},
						"hasSound":True,
						"delayAfterSound":6,
						"soundDelayEndTime":0,
						"soundName":"backflip",
						"beamng":True,
						"hasThirdFunction":False,
						"beamCommand":"hop",
						"argument":"10"
					}
				]

message = ""
user = ""

irc = socket.socket()

irc.connect((SERVER, PORT))
irc.send((	"PASS " + PASS + "\n" +
			"NICK " + BOT + "\n" +
			"JOIN #" + CHANNEL + "\n").encode())

def gamecontrol():
	global message
	ignitionEndTime = 100000000000
	
	printPinMessage()
	while True:
		commandsOnChat()
		secondCommandsAfterDelay()
		thirdCommandsAfterDelay()

		# if "left" == message.lower():
		# 	# ahk.key_down('Left')
		# 	# leftEndTime = time.time() + PRESS_TIME
		# 	# message = ""
		# 	buffer = {
		# 		"name": BEAMMP_NAME,
		# 		"message": "steerLeft",
		# 		"argument": "nil"
		# 	}
		# 	sendToBeamNG(buffer)
		# 	time.sleep(PRESS_TIME)
		# 	buffer = {
		# 		"name": BEAMMP_NAME,
		# 		"message": "stopSteerLeft",
		# 		"argument": "nil"
		# 	}
		# 	sendToBeamNG(buffer)
		# 	message = ""

		# if "right" == message.lower():
		# 	# ahk.key_down('Right')
		# 	# rightEndTime = time.time() + PRESS_TIME
		# 	# message = ""
		# 	buffer = {
		# 		"name": BEAMMP_NAME,
		# 		"message": "steerRight",
		# 		"argument": "nil"
		# 	}
		# 	sendToBeamNG(buffer)
		# 	time.sleep(PRESS_TIME)
		# 	buffer = {
		# 		"name": BEAMMP_NAME,
		# 		"message": "stopSteerRight",
		# 		"argument": "nil"
		# 	}
		# 	sendToBeamNG(buffer)
		# 	message = ""

		# if "upside down" == message.lower(): #only works in freecam
		# 	# ahk.key_down('h')
		# 	# honkEndTime = time.time() + PRESS_TIME
		# 	# message = ""
		# 	buffer = {
		# 		"name": BEAMMP_NAME,
		# 		"message": "cameraUpsideDown",
		# 		"argument": "nil"
		# 	}
		# 	sendToBeamNG(buffer)
		# 	time.sleep(PRESS_TIME)
		# 	buffer = {
		# 		"name": BEAMMP_NAME,
		# 		"message": "stopCameraUpsideDown",
		# 		"argument": "nil"
		# 	}
		# 	sendToBeamNG(buffer)
		# 	message = ""

		if "ignition" == message.lower():
			ahk.key_down('v')
			ignitionEndTime = time.time() + PRESS_TIME
			message = ""

		# if "rain" == message.lower():
		# 	buffer = {
		# 		"name": BEAMMP_NAME,
		# 		"message": "rain",
		# 		"argument": "nil"
		# 	}
		# 	sendToBeamNG(buffer)
		# 	message = ""

		# if "supersonic" == message.lower():
		# 	# playSound("JOHNCENA.mp3", 80)
		# 	# time.sleep(1)
		# 	buffer = {
		# 		"name": BEAMMP_NAME,
		# 		"message": "FOVIncrease",
		# 		"argument": "nil"
		# 	}
		# 	sendToBeamNG(buffer)
		# 	time.sleep(0.5)
		# 	buffer = {
		# 		"name": BEAMMP_NAME,
		# 		"message": "stopFOVIncrease",
		# 		"argument": "nil"
		# 	}
		# 	sendToBeamNG(buffer)
		# 	johnCenaAllowedTime = time.time() + 600
		# 	message = ""

		if time.time() >= ignitionEndTime:
			ahk.key_up('v')
			ignitionEndTime = 100000000000

def printPinMessage():
	print("\n\n\n\n\n\n\n")
	print("/pin Chat commands (commands with capital letters are case sensitive): ")
	for data in BEAMNGCOMMANDS:
		print(data["command"] + ", ")
	print("\n\n\n\n\n\n\n")

def handleSound(commandData):
	buffer = {
		"name": BEAMMP_NAME,
		"message": "playSound",
		"argument": commandData["soundName"]
	}
	sendToBeamNG(buffer)
	commandData["soundDelayEndTime"] = time.time() + commandData["delayAfterSound"]
	return commandData

def commandsOnChat():
	global message
	for data in BEAMNGCOMMANDS:
		if (not data["caseSensitive"] and data["command"] == message.lower()) or (data["caseSensitive"] and data["command"] == message):
			if data["cooldown"]:
				if time.time() < data["cooldownEndTime"]:
					message = "" #this command is still on cooldown
					return
			if data["beamng"]:
				if data["hasSound"]:
					if data["soundDelayEndTime"] == 0:
						handleSound(data)
				if data["hasSound"]:
					if time.time() < data["soundDelayEndTime"]:
						return
					else:
						data["soundDelayEndTime"] = 0
				buffer = {
					"name": BEAMMP_NAME,
					"message": data["beamCommand"],
					"argument": data["argument"]
				}
				sendToBeamNG(buffer)
				if data["hasSecondFunction"]:
					data["secondFunction"]["endTime"] = time.time() + data["pressTime"]
				if data["cooldown"]:
					data["cooldownEndTime"] = time.time() + data["cooldown"]
				# if data["hasSound"]: #kept here for when someone wants a sound effect for the streamer alone
				# 	data["sound"]["endTime"] = time.time() + data["sound"]["delay"]
			message = ""

def secondCommandsAfterDelay(): #this should be a table in the datastructure...
	global message
	for data in BEAMNGCOMMANDS:
		# if data["hasSound"] and time.time() > data["sound"]["endTime"]:
		# 	continue
		if data["hasSecondFunction"] and time.time() > data["secondFunction"]["endTime"]:
			buffer = {
				"name": BEAMMP_NAME,
				"message": data["secondFunction"]["beamCommand"],
				"argument": data["secondFunction"]["argument"]
			}
			sendToBeamNG(buffer)
			data["secondFunction"]["endTime"] = 100000000000
			if data["hasThirdFunction"]:
				data["thirdFunction"]["endTime"] = time.time() + data["secondFunction"]["delay"]
			
def thirdCommandsAfterDelay():
	global message
	for data in BEAMNGCOMMANDS:
		if data["hasThirdFunction"] and time.time() > data["thirdFunction"]["endTime"]:
			buffer = {
				"name": BEAMMP_NAME,
				"message": data["thirdFunction"]["beamCommand"],
				"argument": data["thirdFunction"]["argument"]
			}
			sendToBeamNG(buffer)
			data["thirdFunction"]["endTime"] = 100000000000

def sendToBeamNG(buffer):
	existing_data = []  # Initialize with an empty list

	# Check if the file exists and is not empty
	if os.path.isfile("data.json") and os.path.getsize("data.json") > 0:
		with open("data.json", "rb") as file:
			if file.read(2) != '[]' and file.read(2) != '{}': #https://stackoverflow.com/questions/47792142/how-to-check-if-json-file-contains-only-empty-array
				file.seek(0)  # it may be redundant but it does not hurt
				existing_data = json.load(file)
			# Append the new data to the existing data
	existing_data.append(buffer)
	with open("data.json", "w") as file:
		json.dump(existing_data, file)
		file.close()

def playSound(file, volume = 100):
	soundsPath = "C:\\Users\\Julian\\Documents\\dev\\TwitchPlays\\Sounds\\"
	p = vlc.MediaPlayer("file:///" + soundsPath + file)
	p.audio_set_delay(100)
	p.audio_set_volume(volume)
	p.play()
	

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
		t2. start()
main()