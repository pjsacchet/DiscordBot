# Patrick Sacchet
# Version 1.1
# File implements spotify playing functionality
# TODO: Authentication troubles with Spotify API

import os
import tekore as tk

from discord import Game, Embed
from discord.ext import commands

token_discord = os.getenv("DISCORD_TOKEN")
#conf = tk.config_from_environment()
conf = (str(os.getenv("SPOTIFY_CLIENT_ID")), str(os.getenv("SPOTIFY_SECRET")), str(os.getenv("REDIRECT_URI")))
#client_secret = os.getenv("SPOTIFY_SECRET")
try:
    token_spotify = tk.prompt_for_user_token(*conf, scope=tk.scope.every)
    #token_spotify = tk.request_client_token(*conf[:2])
except Exception:
    pass


#bot = commands.Bot(command_prefix='>tk ', description=description, activity=Game(name=">tk help"))
spotify = tk.Spotify(token_spotify, asynchronous=True)


@bot.command(name='play-sp', help='Play audio from Spotify source')
async def track(ctx, *, query: str = None):
    if query is None:
        await ctx.send("No search query specified")
        return

    tracks, = await spotify.search(query, limit=5)
    embed = Embed(title="Track search results", color=0x1DB954)
    embed.set_thumbnail(url="https://i.imgur.com/890YSn2.png")
    embed.set_footer(text="Requested by " + ctx.author.display_name)

    for t in tracks.items:
        artist = t.artists[0].name
        url = t.external_urls["spotify"]

        message = "\n".join([
            "[Spotify](" + url + ")",
            ":busts_in_silhouette: " + artist,
            ":cd: " + t.album.name
        ])
        embed.add_field(name=t.name, value=message, inline=False)

    await ctx.send(embed=embed)
