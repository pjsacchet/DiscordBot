# DiscordBot
## About
The call for the creation of this bot started when all publicly available bots that played YT videos were taken down. Its also fun to add features to screw with your friends so we do that too!
## Pre Requisites
- Python 3.x.x
  Pip install...
  - discord
  - dotenv (easy to read environment variables)
  - youtube_dl
  - discord 
- ffmpeg.exe (please note - this bot is run via Linux/Linux Kernel for Windows hence this was simply 'sudo apt install'-ed // If on Windows platform make sure this .exe is in your PATH)
## Running the Bot
python3 Vibe.py
## Current Features
- !play
  - Play YouTube links in your server! [please note you must be in a voice channel with VibeBot prior to playing]
- !join
  - Have the bot join your current voice channel [please note you must be in a voice channel first]
- !leave
  - Politely tell VibeBot to leave you alone!
- !pause  
  - Pause the current playing song
- !stop
  - Stop the current playing song all together
- !resume
  - Resume playing the currently paused song
- !commandlist
  - List all commands currently implemented for user
- !updates
  - List most recent and planned updates for user
## Additional Notes
Please note that due to the fact this is a 'bot' it must be actively running at all times if you want it on your server. I'd suggest throwing it on a Pi and keeping it there!
