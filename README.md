# BeamMP-StreamersVsChat
Let your twitch chat wreak havoc on your server.

To make this work you'll need to change some stuff:
- First you need to get your twitch API key (for example [here](https://twitchapps.com/tmi/)). Put the API key (including 'oauth:') into a file named 'DONTOPENMEWHILELIVE.oauth' (create a file with that exact name). 
- Open StreamersVsChat.py and replace everything that says "Julianstap" (my twitch) with your twitch username. Easiest way to do this is have Visual Studio Code, open the .workspace file, press ctrl+f and search for Julianstap and replace all with your username.
- Replace BEAMMP_SERVER_EXE_FOLDER with the folder where your *BeamMP-Server.exe* is located.
- Open .vscode/tasks.json and replace everything that has 'C:/Users/Julian/Desktop/beammp_Server/windows' with the folder where your *BeamMP-Server.exe* is located
- Inside '*BeamMP-Server.exe Location*/Resources/Server/' create a folder named StreamersVsChat

If you want have the commands only apply on you, change BEAMMP_NAME to your beammp username.

After all these changes press 'ctrl+shift+p' and run the tasks 'Copy server' and 'Compress client'. Next right click on 'StreamersVsChat.py' and click 'Run Python File in Terminal'. It will print out all available twitch chat commands in the terminal.
Now you are ready to start the server and receive commands from the twitch chat (you can test this without streaming).
