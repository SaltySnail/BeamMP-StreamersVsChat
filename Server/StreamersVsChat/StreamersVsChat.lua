players = {} --table to hold information about players

local possibleCommands = {} --linking commands to client functions
possibleCommands["playSound"] = "onPlaySound"
possibleCommands["hop"] = "onJump"
possibleCommands["boost"] = "onSpeedBoost"
possibleCommands["johncena"] = "onJohnCena"
possibleCommands["moon"] = "onMoonGravity"
possibleCommands["earth"] = "onEarthGravity"
possibleCommands["warningSignal"] = "onWarningSignal"
possibleCommands["siren"] = "onSiren"
possibleCommands["drift"] = "onDrift"
possibleCommands["stopDrift"] = "onStopDrift"
possibleCommands["gas"] = "onGas"
possibleCommands["stopGas"] = "onStopGas"
possibleCommands["brake"] = "onBrake"
possibleCommands["stopBrake"] = "onStopBrake"
possibleCommands["honk"] = "onHonk"
possibleCommands["stopHonk"] = "onStopHonk"
possibleCommands["clutch"] = "onClutch"
possibleCommands["stopClutch"] = "onStopClutch"
possibleCommands["handbrake"] = "onHandbrake"
possibleCommands["stopHandbrake"] = "onStopHandbrake"
possibleCommands["steerLeft"] = "onSteerLeft"
possibleCommands["stopSteerLeft"] = "onStopSteerLeft"
possibleCommands["steerRight"] = "onSteerRight"
possibleCommands["stopSteerRight"] = "onStopSteerRight"
possibleCommands["lookBack"] = "onLookBack"
possibleCommands["stopLookBack"] = "onStopLookBack"
possibleCommands["lookLeft"] = "onLookLeft"
possibleCommands["stopLookLeft"] = "onStopLookLeft"
possibleCommands["lookRight"] = "onLookRight"
possibleCommands["stopLookRight"] = "onStopLookRight"
possibleCommands["blind"] = "onBlind"
possibleCommands["stopBlind"] = "onStopBlind"
possibleCommands["FOVIncrease"] = "onFOVIncrease"
possibleCommands["stopFOVIncrease"] = "onStopFOVIncrease"
possibleCommands["changeCamera"] = "onChangeCamera"
possibleCommands["lights"] = "onLights"
possibleCommands["DO A BARREL ROLL!"] = "onBarrelRoll"
possibleCommands["spin"] = "onSpin"
possibleCommands["explode"] = "onExplode"
possibleCommands["ice"] = "onIce"
possibleCommands["stopIce"] = "onStopIce"
possibleCommands["backflip"] = "onBackflip"

function dump(o)
    if type(o) == 'table' then
       local s = '{ '
       for k,v in pairs(o) do
          if type(k) ~= 'number' then k = '"'..k..'"' end
          s = s .. '['..k..'] = ' .. dump(v) .. ','
       end
       return s .. '} '
    else
       return tostring(o)
    end
end

function svcTimer()
	if not players then return end
	local file = io.open("StreamersVsChatData.json", "r")
	local content = file:read("*all")
	file:close()
	file = io.open("StreamersVsChatData.json", "w") --overwrite file
	file:close()
	
	if not content or content == "" then return end
	
	local allData = Util.JsonDecode(content)
	if not allData then return end
	
	-- print(dump(allData))
	-- Iterate over each table in allData
	for i, data in ipairs(allData) do
		-- print(dump(data))
		-- Now you can access the fields of each table
		for id, player in pairs(players) do
			if player.name == data["name"] or data["name"] == "-1" then
				if data["name"] == "-1" then
					id = -1
				end
				print(id .. " " .. player.name .. " " .. possibleCommands[data["message"]])
				MP.TriggerClientEvent(id, possibleCommands[data["message"]], data["argument"])
				if id == -1 then return end
			end
		end
	end
end

function onInit() 
	MP.RegisterEvent("onPlayerAuth", "onPlayerAuth")
	MP.RegisterEvent("onPlayerConnecting", "onPlayerConnecting")
	MP.RegisterEvent("onPlayerJoining", "onPlayerJoining")
	MP.RegisterEvent("onPlayerJoin", "onPlayerJoin")
	MP.RegisterEvent("onPlayerDisconnect", "onPlayerDisconnect")
	MP.RegisterEvent("onChatMessage", "onChatMessage")
	MP.RegisterEvent("onVehicleSpawn", "onVehicleSpawn")
	MP.RegisterEvent("onVehicleEdited", "onVehicleEdited")
	MP.RegisterEvent("onVehicleReset", "onVehicleReset")
	MP.RegisterEvent("onVehicleDeleted", "onVehicleDeleted")
	
	--Custom
	MP.RegisterEvent("onJump", "onJump")
	MP.RegisterEvent("onSpeed", "onSpeed")

	MP.CancelEventTimer("counter")
	MP.CancelEventTimer("svcTrigger") --svc for StreamersVsChat
	MP.CreateEventTimer("svcTrigger", 50) --check commands every 50ms
	MP.RegisterEvent("svcTrigger", "svcTimer")
	
	print("--------------------StreamersVsChat loaded")

end

--A player has authenticated and is requesting to join
--The player's name (string), forum role (string), guest account (bool), identifiers (table -> ip, beammp)
function onPlayerAuth(player_name, role, isGuest, identifiers)
	--print("onPlayerAuth: player_name: " .. player_name .. " | role: " .. role .. " | isGuest: " .. tostring(isGuest) .. " | ip: " .. ip .. " | beammp: " .. beammp)
	players[player_name] = {
		["name"] = player_name,
		["role"] = role,
		["isGuest"] = isGuest,
		["identifiers"] = identifiers
	}
end

--A player is loading in (Before loading the map)
--The player's ID (number)
function onPlayerConnecting(player_id)
	player_name = MP.GetPlayerName(player_id)
	players[player_id] = players[player_name]
	players[player_id].id = player_id
	players[player_name] = nil
end

--A player is loading the map and will be joined soon
--The player's ID (number)
function onPlayerJoining(player_id)
	
end

--A player has joined and loaded in
--The player's ID (number)
function onPlayerJoin(player_id)
	MP.SendChatMessage(-1, players[player_id].name .. " has joined the server!")
	players[player_id].vehicles = {}
end

--A player has disconnected
--The player's ID (number)
function onPlayerDisconnect(player_id)
	MP.SendChatMessage(-1, players[player_id].name .. " has left the server!")
	players[player_id] = nil
end

--A chat message was sent
--The sender's ID, the sender's name, and the chat message
function onChatMessage(player_id, player_name, message)
	if message:sub(1,1) == commandPrefix then --if the character at index 1 of the string is the command prefix then
		command = string.sub(message,2) --the command is everything in the chat message from string index 2 to the end of the string
		onCommand(player_id, command) --call the onCommand() function passing in the player's ID and the command string
		return 1 --prevent the command from showing up in the chat
	else --otherwise do nothing
	end
end

function onVehicleSpawn(player_id, vehicle_id, data)
	local s = data:find('%{')
	data = data:sub(s)
	data = Util.JsonDecode(data)
	players[player_id].vehicles[vehicle_id] = data.jbm
end

function onVehicleEdited(player_id, vehicle_id, data)
	local s = data:find('%{')
	data = data:sub(s)
	data = Util.JsonDecode(data)
	players[player_id].vehicles[vehicle_id] = data.jbm
end

function onVehicleReset(player_id, vehicle_id, data)

end

function onVehicleDeleted(player_id, vehicle_id)
	players[player_id].vehicles[vehicle_id] = nil
end
