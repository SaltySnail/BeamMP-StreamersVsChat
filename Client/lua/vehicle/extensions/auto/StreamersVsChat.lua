-- VElua
M = {}

local originalClutchLockTorque = 0
local originalOutputAV1 = 0

function onDrift()
    -- Your function logic here
    print("onDrift called")
    -- originalClutchLockTorque = electrics.values.wheelspeed
    -- electrics.values.wheelspeed = originalClutchLockTorque * 200
    -- print(dump(FS:findFiles("/art/sound/", "*.mp3", -1, true, false)))
    -- print(dump(soundFiles))
    -- print(dump(sfxSources))
    -- obj:setVolume(sfxSources["drift"], 1) 
    -- obj:playSFX(sfxSources["drift"])
    originalClutchLockTorque = powertrain.getDevice("clutch").lockTorque
    originalOutputAV1 = powertrain.getDevice("mainEngine").outputAV1
    powertrain.getDevice("clutch").lockTorque = originalClutchLockTorque * 10
    powertrain.getDevice("mainEngine").outputAV1 = originalOutputAV1 * 3
end

function onStopDrift()
    print("onStopDrift called " .. originalOutputAV1 .. " " .. originalClutchLockTorque)
    -- electrics.values.wheelspeed = originalClutchLockTorque
    powertrain.getDevice("mainEngine").outputAV1 = originalOutputAV1
    powertrain.getDevice("clutch").lockTorque = originalClutchLockTorque
end

function onGas()
    print("onGas called")
    input.event("throttle", 1, "FILTER_AI")
end

function onStopGas()
    print("onStopGas called")
    input.event("throttle", 0, "FILTER_AI")
end

function onSteerRight()
    print("onSteerRight called")
    input.event("steering", 1, "FILTER_DIRECT")
end

function onSteerLeft()
    print("onSteerLeft called")
    input.event("steering", -1, "FILTER_DIRECT")
end

function onStopSteerRight()
    print("onStopSteerRight called")
    input.event("steering", 0, "FILTER_DIRECT")
end

function onStopSteerLeft()
    print("onStopSteerLeft called")
    input.event("steering", 0, "FILTER_DIRECT")
end

function onBrake()
    print("onBrake called")
    input.event("brake", 1, "FILTER_AI")
end

function onStopBrake()
    print("onStopBrake called")
    input.event("brake", 0, "FILTER_AI")
end

function onHonk()
    print("onHonk called")
    electrics.horn(true)
end

function onStopHonk()
    print("onStopHonk called")
    electrics.horn(false)
end

function onClutch()
    print("onClutch called")
    input.event("clutch", 1, "FILTER_AI")
end

function onStopClutch()
    print("onStopClutch called")
    input.event("clutch", 0, "FILTER_AI")
end

function onHandbrake()
    print("onHandbrake called")
    input.event("parkingbrake", 1, "FILTER_AI")
end

function onStopHandbrake()
    print("onStopHandbrake called")
    input.event("parkingbrake", 0, "FILTER_AI")
end

function onSiren()
    print("onSiren called")
    electrics.toggle_lightbar_signal()
end

function onEarthGravity()
    print("onEarthGravity called")
    obj:setGravity(-9.81)
end

function onMoonGravity()
    print("onMoonGravity called")
    obj:setGravity(-1.62)
end

function onWarningSignal()
    print("onWarningSignal called")
    electrics.toggle_warn_signal()
end

function onLights()
    print("onLights called")
    electrics.toggle_lights()
end

function onSpeedBoost(data)
	print("onSpeedBoost Called") --debug print so we can check in-game console
	local height
	if data then
		if data ~= "null" and data ~= "nil" then
			height = tonumber(data)
		end
	end
	if not height then --if no height argument is provided then
		height = 5 --set height to 5
	end
	-- local veh = be:getPlayerVehicle(0) --get the player's current vehicle as an object
	local position = vec3(obj:getPosition())

	-- Get the vehicle's forward direction vector
	local forward = vec3(obj:getDirectionVector():normalized())

	-- Define the distance to move the vehicle forwardwards
	local distance = height

	-- Calculate the new position
	local newPosition = forward * distance

	-- Set the vehicle's position to the new position
	velocityVE.addAngularVelocity(newPosition.x, newPosition.y, newPosition.z, 0, 0, 0)
end

function onJump(data)
	print("onJump Called") --debug print so we can check in-game console
	local height
	if data then
		if data ~= "null" and data ~= "nil" then
			height = tonumber(data)
		end
	end
	if not height then --if no height argument is provided then
		height = 5 --set height to 1
	end
	print("onJump Called: " .. height .. " meters") --debug print so we can check in-game console
	velocityVE.addAngularVelocity(0, 0, height, 0, 0, 0)
end

function onBarrelRoll(data)
	local height
	if data then
		if data ~= "null" and data ~= "nil" then
			local buffer = tonumber(data)
			if buffer then
				height = buffer --get height (in meters) from the data sent by !jump command
			end
		end
	end
	if not height then --if no height argument is provided then
		height = 5 --set height to 5
	end
	print("onBarrelRoll Called: " .. height .. " meters") --debug print so we can check in-game console
	local position = vec3(obj:getPosition())

	-- Get the vehicle's forward direction vector
	local forward = vec3(obj:getDirectionVector():normalized())

	-- Define the force to rotate around the vehicle forward vector with
	local distance = height

	-- Calculate the new position
	local newPosition = forward * distance

	-- Set the vehicle's position to the new position
	velocityVE.addAngularVelocity(0, 0, 0, newPosition.x, newPosition.y, newPosition.z)
end

function onSpin(data)
	local height
	if data then
		if data ~= "null" and data ~= "nil" then
			local buffer = tonumber(data)
			if buffer then
				height = buffer --get height (in meters) from the data sent by !jump command
			end
		end
	end
	if not height then --if no height argument is provided then
		height = 5 --set height to 5
	end
	print("onSpin Called: " .. height .. " meters") --debug print so we can check in-game console
	local position = vec3(obj:getPosition())

	-- Get the vehicle's upward direction vector
	local upward = vec3(obj:getDirectionVectorUp():normalized())

	-- Define the force to rotate around the vehicle upward vector with
	local distance = height

	-- Calculate the new position
	local newPosition = upward * distance

	-- Set the vehicle's position to the new position
	velocityVE.addAngularVelocity(0, 0, 0, newPosition.x, newPosition.y, newPosition.z)
end

function onBackflip(data)
	local height
	if data then
		if data ~= "null" and data ~= "nil" then
			local buffer = tonumber(data)
			if buffer then
				height = buffer --get height (in meters) from the data sent by !jump command
			end
		end
	end
	if not height then --if no height argument is provided then
		height = 5 --set height to 5
	end
	print("onBackflip Called: " .. height .. " meters") --debug print so we can check in-game console
	-- Get the vehicle's right direction vector
	local right = vec3(obj:getDirectionVectorRight():normalized())

	-- Define the force to rotate around the vehicle right vector with
	local distance = height

	-- Calculate the new position
	local newPosition = right * distance

	-- Set the vehicle's position to the new position
	velocityVE.addAngularVelocity(0, 0, 0, newPosition.x, newPosition.y, newPosition.z)
end

function onExplode()
    fire.explodeVehicle()
    fire.igniteVehicle()
    beamstate.breakAllBreakgroups()
end

function onIce()
	print("onIce called")
	for i=0,#wheels.wheelRotators do
        local wheel = obj:getWheel(i)
        if wheel then
			wheel:setFrictionThermalSensitivity(
				-300,       -- frictionLowTemp              default: -300
				1e7,        -- frictionHighTemp             default: 1e7
				1e-10,      -- frictionLowSlope             default: 1e-10
				1e-10,      -- frictionHighSlope            default: 1e-10
				10,         -- frictionSlopeSmoothCoef      default: 10
				0.1,   -- frictionCoefLow              default: 1
				0.1,   -- frictionCoefMiddle           default: 1
				0.1    -- frictionCoefHigh             default: 1
			)
		end
	end
end

local function resetTyreGrip()
	for i=0,#wheels.wheelRotators do
        local wheel = obj:getWheel(i)
        if wheel then
			wheel:setFrictionThermalSensitivity(
				-300,       -- frictionLowTemp              default: -300
				1e7,        -- frictionHighTemp             default: 1e7
				1e-10,      -- frictionLowSlope             default: 1e-10
				1e-10,      -- frictionHighSlope            default: 1e-10
				10,         -- frictionSlopeSmoothCoef      default: 10
				1,   -- frictionCoefLow              default: 1
				1,   -- frictionCoefMiddle           default: 1
				1    -- frictionCoefHigh             default: 1
			)
		end
	end
end

function onStopIce()
	print("onStopIce called")
	resetTyreGrip()
end

function onIgnitionOff()
	print("onIgnitionOff called")
	electrics.setIgnitionLevel(0)
end

function onIgnitionOn()
	print("onIgnitionOn called")
	electrics.setIgnitionLevel(3)
end

-- Expose the function to GElua
-- beamngVehicle = {}
-- beamngVehicle.onDrift = M.onDrift
M.onDrift = onDrift
M.onStopDrift = onStopDrift
M.onGas = onGas
M.onStopGas = onStopGas
M.onClutch = onClutch
M.onStopClutch = onStopClutch
M.onSteerLeft = onSteerLeft
M.onSteerRight = onSteerRight
M.onStopBrake = onStopBrake
M.onBrake = onBrake
M.onStopSteerLeft = onStopSteerLeft
M.onStopSteerRight = onStopSteerRight
M.onHonk = onHonk
M.onStopHonk = onStopHonk
M.onHandbrake = onHandbrake
M.onStopHandbrake = onStopHandbrake
M.onSiren = onSiren
M.onWarningSignal = onWarningSignal
M.onMoonGravity = onMoonGravity
M.onEarthGravity = onEarthGravity
M.onWarningSignal = onWarningSignal
M.onLights = onLights
M.onSpeedBoost = onSpeedBoost
M.onJump = onJump
M.onBarrelRoll = onBarrelRoll
M.onSpin = onSpin
M.onExplode = onExplode
M.onIce = onIce
M.onStopIce = onStopIce
M.onBackflip = onBackflip
M.onIgnitionOff = onIgnitionOff
M.onIgnitionOn = onIgnitionOn

return M