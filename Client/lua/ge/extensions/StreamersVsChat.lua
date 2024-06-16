local M = {} --metatable

local curFOV = 0

-- local soundFiles = {}
-- -- Initialize sound
-- soundFiles.barrelroll = "art/sound/barrelroll"
-- soundFiles.blind = "/art/sound/blind"
-- soundFiles.boost = "/art/sound/GASGASGAS"
-- soundFiles.johncena = "art/sound/JOHNCENA"
-- soundFiles.drift = "/art/sound/tokyo"

function onPlaySound(data)
	Engine.Audio.playOnce('AudioGui', "/art/sound/" .. data, {volume = 65})
end

function onJump(data)
	print("onJump Called") --debug print so we can check in-game console
	be:queueAllObjectLua("if StreamersVsChat then StreamersVsChat.onJump(" .. data .. ") end")
end

function onSpeedBoost(data)	
	print("onSpeedBoost Called") --debug print so we can check in-game console
	be:queueAllObjectLua("if StreamersVsChat then StreamersVsChat.onSpeedBoost(" .. data .. ") end")
end

function onBarrelRoll(data)	
	print("onBarrelRoll Called") --debug print so we can check in-game console
	be:queueAllObjectLua("if StreamersVsChat then StreamersVsChat.onBarrelRoll(" .. data .. ") end")
end

function onSpin(data)	
	print("onSpin Called") --debug print so we can check in-game console
	be:queueAllObjectLua("if StreamersVsChat then StreamersVsChat.onSpin(" .. data .. ") end")
end

function onEarthGravity()	
	print("onEarthGravity Called") 
	be:queueAllObjectLua("if StreamersVsChat then StreamersVsChat.onEarthGravity() end")
end

function onMoonGravity()	
	print("onMoonGravity Called")
	be:queueAllObjectLua("if StreamersVsChat then StreamersVsChat.onMoonGravity() end")
end

function onWarningSignal()	
	print("onWarningSignal Called")
	be:queueAllObjectLua("if StreamersVsChat then StreamersVsChat.onWarningSignal() end")
end

function onDrift()
	print("onDrift Called")
	be:queueAllObjectLua("if StreamersVsChat then StreamersVsChat.onDrift() end")
	-- Engine.Audio.playOnce('AudioGui', soundFiles.drift, {volume = 100})
end

function onStopDrift()
	print("onStopDrift Called") 
	be:queueAllObjectLua("if StreamersVsChat then StreamersVsChat.onStopDrift() end")
end

function onGas()
	print("onGas Called")
	be:queueAllObjectLua("if StreamersVsChat then StreamersVsChat.onGas() end")
end

function onStopGas()
	print("onStopGas Called") 
	be:queueAllObjectLua("if StreamersVsChat then StreamersVsChat.onStopGas() end")
end

function onHonk()
	print("onHonk Called")
	be:queueAllObjectLua("if StreamersVsChat then StreamersVsChat.onHonk() end")
end

function onStopHonk()
	print("onStopHonk Called") 
	be:queueAllObjectLua("if StreamersVsChat then StreamersVsChat.onStopHonk() end")
end

function onHandbrake()
	print("onHandbrake Called")
	be:queueAllObjectLua("if StreamersVsChat then StreamersVsChat.onHandbrake() end")
end

function onStopHandbrake()
	print("onStopHandbrake Called") 
	be:queueAllObjectLua("if StreamersVsChat then StreamersVsChat.onStopHandbrake() end")
end

function onClutch()
	print("onClutch Called")
	be:queueAllObjectLua("if StreamersVsChat then StreamersVsChat.onClutch() end")
end

function onStopClutch()
	print("onStopClutch Called") 
	be:queueAllObjectLua("if StreamersVsChat then StreamersVsChat.onStopClutch() end")
end

function onBrake()
	print("onBrake Called")
	be:queueAllObjectLua("if StreamersVsChat then StreamersVsChat.onBrake() end")
end

function onStopBrake()
	print("onStopBrake Called") 
	be:queueAllObjectLua("if StreamersVsChat then StreamersVsChat.onStopBrake() end")
end

function onSteerLeft()
	print("onSteerLeft Called")
	be:queueAllObjectLua("if StreamersVsChat then StreamersVsChat.onSteerLeft() end")
end

function onStopSteerLeft()
	print("onStopSteerLeft Called") 
	be:queueAllObjectLua("if StreamersVsChat then StreamersVsChat.onStopSteerLeft() end")
end

function onSteerRight()
	print("onSteerRight Called")
	be:queueAllObjectLua("if StreamersVsChat then StreamersVsChat.onSteerRight() end")
end

function onStopSteerRight()
	print("onStopSteerRight Called") 
	be:queueAllObjectLua("if StreamersVsChat then StreamersVsChat.onStopSteerRight() end")
end

function onChangeCamera()
	print("onChangeCamera Called") 
	core_camera.setVehicleCameraByIndexOffset(0, 1)
end

-- function onRain()
-- 	core_weather.switchWeather('rain')
-- end

-- function onCameraUpsideDown()
-- 	core_camera.rollAbs(180)
-- end

-- function onStopCameraUpsideDown()
-- 	core_camera.rollAbs(0)
-- end

function onLookBack()
	print("onLookBack Called") 
	core_camera.setLookBack(nil, true) --player = nil, value = true (player isn't used in the function)
end

function onStopLookBack()
	print("onStopLookBack Called") 
	core_camera.setLookBack(nil, false)
end

function onLookRight()
	print("onLookRight Called") 
	core_camera.rotate_yaw(90, "FILTER_PAD")
end

function onStopLookRight()
	print("onStopLookRight Called") 
	core_camera.rotate_yaw(0, "FILTER_PAD") --should be combined with onStopLookLeft as cameraReset
end

function onLookLeft()
	print("onLookLeft Called") 
	core_camera.rotate_yaw(-90, "FILTER_PAD")
end

function onStopLookLeft()
	print("onStopLookLeft Called") 
	core_camera.rotate_yaw(0, "FILTER_PAD")
end

function onScreenRGB(arg)
	print("onScreenRGB Called") 
	scenetree["PostEffectCombinePassObject"]:setField("enableBlueShift", 0, 1)
	scenetree["PostEffectCombinePassObject"]:setField("blueShiftColor", 0, arg)
	-- Engine.Audio.playOnce('AudioGui', soundFiles.blind, {volume = 100})
end

function onStopScreenRGB(arg)
	print("onStopScreenRGB Called") 
	scenetree["PostEffectCombinePassObject"]:setField("enableBlueShift", 0, 0) --blueShift is the colorShift of the screen, glad naming things is hard for the beam team as well.
	scenetree["PostEffectCombinePassObject"]:setField("blueShiftColor", 0, arg)
end

function onLights()
	print("onLights Called") 
	be:queueAllObjectLua("if StreamersVsChat then StreamersVsChat.onLights() end")
end

function onExplode()
	print("onExplode Called") 
	be:queueAllObjectLua("if StreamersVsChat then StreamersVsChat.onExplode() end")
end

function onIce()
	print("onIce Called") 
	be:queueAllObjectLua("if StreamersVsChat then StreamersVsChat.onIce() end")
end

function onStopIce()
	print("onStopIce Called") 
	be:queueAllObjectLua("if StreamersVsChat then StreamersVsChat.onStopIce() end")
end

function onBackflip(data)
	print("onBackflip Called") 
	be:queueAllObjectLua("if StreamersVsChat then StreamersVsChat.onBackflip(" .. data .. ") end")
end

function onSiren()
	print("onSiren Called") 
	be:queueAllObjectLua("if StreamersVsChat then StreamersVsChat.onSiren() end")
end

function onIgnitionOff()
	print("onIgnitionOff Called") 
	be:queueAllObjectLua("if StreamersVsChat then StreamersVsChat.onIgnitionOff() end")
end

function onIgnitionOn()
	print("onIgnitionOn Called") 
	be:queueAllObjectLua("if StreamersVsChat then StreamersVsChat.onIgnitionOn() end")
end

-- function onFOVIncrease()
-- 	print("onFOVIncrease Called") 
-- 	curFOV = core_camera.getFovDeg()
-- 	print(dump(be:getPlayerVehicle(0)))
-- 	core_camera.setFOV(curFOV * 10)
-- end

-- function onStopFOVIncrease()
-- 	print("onStopFOVIncrease Called") 
-- 	core_camera.setFOV(curFOV)
-- end


local function onExtensionLoaded()
	-- print("--------------------Loading examplePlugin") --debug print so we can check in-game console
	-- AddEventHandler("jump", onJump) --name of event to call (string), and the function that calling this event will process
	-- AddEventHandler("speed", onSpeed) --so, in this example, when the server triggers the client event "speed", the client does the onSpeed function
	AddEventHandler("onPlaySound", onPlaySound)
	AddEventHandler("onJump", onJump)
	AddEventHandler("onSpeedBoost", onSpeedBoost)
	AddEventHandler("onMoonGravity", onMoonGravity)
	AddEventHandler("onEarthGravity", onEarthGravity)
	AddEventHandler("onDrift", onDrift)
	AddEventHandler("onStopDrift", onStopDrift)
	AddEventHandler("onStopGas", onStopGas)
	AddEventHandler("onGas", onGas)
	AddEventHandler("onStopClutch", onStopClutch)
	AddEventHandler("onClutch", onClutch)
	-- AddEventHandler("onRain", onRain)
	AddEventHandler("onBarrelRoll", onBarrelRoll)
	AddEventHandler("onSteerLeft", onSteerLeft)
	AddEventHandler("onSteerRight", onSteerRight)
	AddEventHandler("onStopBrake", onStopBrake)
	AddEventHandler("onBrake", onBrake)
	AddEventHandler("onStopSteerLeft", onStopSteerLeft)
	AddEventHandler("onStopSteerRight", onStopSteerRight)
	AddEventHandler("onHonk", onHonk)
	AddEventHandler("onStopHonk", onStopHonk)
	AddEventHandler("onHandbrake", onHandbrake)
	AddEventHandler("onStopHandbrake", onStopHandbrake)
	AddEventHandler("onWarningSignal", onWarningSignal)
	AddEventHandler("onSiren", onSiren)
	-- AddEventHandler("onCameraUpsideDown", onCameraUpsideDown)
	-- AddEventHandler("onStopCameraUpsideDown", onStopCameraUpsideDown)
	AddEventHandler("onLookBack", onLookBack)
	AddEventHandler("onStopLookBack", onStopLookBack)
	AddEventHandler("onLookRight", onLookRight)
	AddEventHandler("onStopLookRight", onStopLookRight)
	AddEventHandler("onLookLeft", onLookLeft)
	AddEventHandler("onStopLookLeft", onStopLookLeft)
	AddEventHandler("onScreenRGB", onScreenRGB)
	AddEventHandler("onStopScreenRGB", onStopScreenRGB)
	AddEventHandler("onFOVIncrease", onFOVIncrease)
	AddEventHandler("onStopFOVIncrease", onStopFOVIncrease)
	AddEventHandler("onChangeCamera", onChangeCamera)
	AddEventHandler("onLights", onLights)
	AddEventHandler("onSpin", onSpin)
	AddEventHandler("onExplode", onExplode)
	AddEventHandler("onIce", onIce)
	AddEventHandler("onStopIce", onStopIce)
	AddEventHandler("onBackflip", onBackflip)
	AddEventHandler("onIgnitionOff", onIgnitionOff)
	AddEventHandler("onIgnitionOn", onIgnitionOn)
end

M.onExtensionLoaded = onExtensionLoaded --these are exposed globally via the metatable so that they can be called by the game itself
M.onPlaySound = onPlaySound

M.onJump = onJump
M.onSpeedBoost = onSpeedBoost
M.onEarthGravity = onEarthGravity
M.onMoonGravity = onMoonGravity
M.onDrift = onDrift
-- M.onRain = onRain
M.onStopDrift = onStopDrift
M.onBarrelRoll = onBarrelRoll
M.onGas = onGas
M.onSteerLeft = onSteerLeft
M.onSteerRight = onSteerRight
M.onStopBrake = onStopBrake
M.onBrake = onBrake
M.onStopSteerLeft = onStopSteerLeft
M.onStopSteerRight = onStopSteerRight
M.onStopGas = onStopGas
M.onHonk = onHonk
M.onStopHonk = onStopHonk
M.onClutch = onClutch
M.onStopClutch = onStopClutch
M.onHandbrake = onHandbrake
M.onStopHandbrake = onStopHandbrake
M.onWarningSignal = onWarningSignal
M.onSiren = onSiren
-- M.onStopCameraUpsideDown = onStopCameraUpsideDown
-- M.onCameraUpsideDown = onCameraUpsideDown
M.onStopLookBack = onStopLookBack
M.onLookBack = onLookBack
M.onStopLookRight = onStopLookRight
M.onLookRight = onLookRight
M.onStopLookLeft = onStopLookLeft
M.onLookLeft = onLookLeft
M.onStopScreenRGB = onStopScreenRGB
M.onScreenRGB = onScreenRGB
M.onStopFOVIncrease = onStopFOVIncrease
M.onFOVIncrease = onFOVIncrease
M.onChangeCamera = onChangeCamera
M.onLights = onLights
M.onSpin = onSpin
M.onExplode = onExplode
M.onIce = onIce
M.onStopIce = onStopIce
M.onBackflip = onBackflip
M.onIgnitionOff = onIgnitionOff
M.onIgnitionOn = onIgnitionOn

return M --return the metatable