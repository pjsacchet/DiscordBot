# Patrick Sacchet
# VERSION 1.1
# This version is the initial release of our new bot - it will be able to play music since all the other music bots are dead :(
# Implements some features of main funcitonality, to include main join/leave functionality, play/pause/resume, help, and basic message checks
import os
import discord
from discord.ext import commands,tasks
from dotenv import load_dotenv
import random
import youtube_dl

from discord.utils import get
from youtube_dl import YoutubeDL
from discord import FFmpegPCMAudio

# Roll to see if we mock the user sending messages in the channel, if we do, grab a random message
def mock_user():
    random_num = random.randint(1, 10)

    if (random_num == 2):
        # Get random response from list of responses
        fileObj = open("Responses.txt", "r")
        responses = fileObj.read().splitlines()
        fileObj.close()
        response = str(random.choice(responses))
        return response

    return None

def main():
    print("VIBE CHECK")
    load_dotenv()
    # You need your own bot token ...
    TOKEN = os.getenv('DISCORD_TOKEN')

    # Client represents a connection to Discord - handles events, tracks state, and interacts with Discord APIs
    intents = discord.Intents().all()
    client = discord.Client(intents=intents)

    # If a user wants to run a command they must prefix with a '!'
    bot = commands.Bot(command_prefix='!', intents=intents)

    # Send list of most recent updates to user
    @bot.command(name='updates', help='List recent updates for user')
    async def updates(ctx):
        with open("Updates.txt", "r") as file:
            contents = file.read()
            file.close()
        await ctx.send(str(contents))

    # Send list of commands to user
    @bot.command(name='commandlist', help='List all commands for user')
    async def commandlist(ctx):
        with open("Commands.txt", "r") as file:
            contents = file.read()
            file.close()
        await ctx.send(str(contents))

    # Have the bot join the channel the user is currently in
    @bot.command(name='join', help='Tells VibeBot to join the voice channel')
    async def join(ctx):

        if (not ctx.message.author.voice):
            await ctx.send("{} is not connected to the voice channel".format(ctx.author.name))
            return

        else:
            channel = ctx.message.author.voice.channel

        await channel.connect()

    # Have the bot leave the channel its currently in (and check to make sure its connected to a channel)
    @bot.command(name='leave', help='To make the bot leave the voice channel')
    async def leave(ctx):
        voice_client = ctx.message.guild.voice_client

        if (voice_client.is_connected()):
            await voice_client.disconnect()

        else:
            await ctx.send("The bot is not connected to a voice channel")

    # Play a song (and make sure we aren't already playing something)
    @bot.command(name='play', help='Play audio from YouTube source')
    async def play(ctx, url):
        YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
        FFMPEG_OPTIONS = {
            'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        voice = get(bot.voice_clients, guild=ctx.guild)

        if (not voice.is_playing()):
            with YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(url, download=False)
            URL = info['url']
            voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
            voice.is_playing()
            await ctx.send('Bot is playing')

        else:
            await ctx.send("Bot is already playing")
            return

    # Pause the song currently playing (and check if there was one playing in the first place)
    @bot.command(name='pause', help='Pause the song currently playing')
    async def pause(ctx):
        voice_client = ctx.message.guild.voice_client

        if (voice_client.is_playing()):
            await voice_client.pause()

        else:
            await ctx.send("The bot is not playing anything at the moment.")

    # Resume the song that was previously playing (and check if there was one in the first place)
    @bot.command(name='resume', help='Resume the song currently paused')
    async def resume(ctx):
        voice_client = ctx.message.guild.voice_client

        if (voice_client.is_paused()):
            await voice_client.resume()

        else:
            await ctx.send("The bot was not playing anything before this. Use play_song command")

    # Stop the song currently playing (and check if its even playing in the first place)
    @bot.command(name='stop', help='Stops the song currently playing')
    async def stop(ctx):
        voice_client = ctx.message.guild.voice_client

        if (voice_client.is_playing()):
            await voice_client.stop()

        else:
            await ctx.send("The bot is not playing anything at the moment.")

    # On ready event handler, which handles event when client has established a connection to Discord and it has finished preparing the data Discord has sent
    # AKA on_ready will be called when client is ready for further instruction
    @bot.event
    async def on_ready():
        print(f'{bot.user} has connected to the server!')

    # When a message is sent to the server...
    @bot.event
    async def on_message(message):
        # If its another bot on the server don't respond
        if (message.author == bot.user):
            return

        # If its Adam respond appropiately
        if (str(message.author) == os.getenv('ADAM_USERNAME')):
            response = mock_user()
            if (response != None):
                await message.channel.send(response)

        # If someone is calling for dongers to be raised make sure we raise them
        if ('raise' in message.content.lower() and 'dongers' in message.content.lower()):
            possible_dongers = ["ヽ༼ຈل͜ຈ༽ﾉ", "ヽ༼◉ل͜◉༽ﾉ", "ヽ༼◔ل͜◔༽ﾉ", "ヽ༼⊙ل͜⊙༽ﾉ", "ヽ༼☉ل͜☉༽ﾉ", "ヽ༼ಠل͜ಠ༽ﾉ", "ヽ༼இل͜இ༽ﾉ", "ヽ༼≖ل͜≖༽ﾉ", "ヽ༼ຈ益ຈ༽ﾉ", " ༼ᕗຈل͜ຈ༽ᕗ", "╮(╯ل͜╰)╭ ", "ヽ༼ ͠° ͟ل͜ ͠° ༽ﾉ", "ヽ༼° ل͜ °༽ﾉ", "ヽ༼ಸ ل͜ ಸ༽ﾉ", "ヽ༼ ・ ل͜ ・ ༽ﾉ ", "ຈلຈ", "ᕦ༼༎ຶ_༎ຶ༽ᕗ", "┬┴┬┴༼ ಥل͟ಥ ༽ ┬┴┬┴┤", "( ͡° ͜ʖ ͡°)", "ಠ_ಠ", "¯\_(ツ)_/¯"]
            response = "DONGERS BE RAISED " + random.choice(possible_dongers)
            await message.channel.send(response)

        # on_message overwrites + prevents any calls to process_commands (meaning it will not listen for commands) so we have to call it manually after checking the messages sent to the server
        await bot.process_commands(message)

    bot.run(TOKEN)


if __name__ == '__main__':
    main()
