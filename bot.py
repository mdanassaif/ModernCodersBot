import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

# ***REPLACE THIS WITH YOUR ACTUAL BOT TOKEN***
TOKEN = os.environ.get("TOKEN")  # Get token from environment variable

# ***REPLACE THIS WITH YOUR MUSIC BOT CHANNEL ID***
music_bot_channel_id = 123456789012345678

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} has connected to Discord!")

@bot.command()
async def gartic(ctx):
    await ctx.send("Join the Gartic.io game here: [link to gartic.io or your hosted game]")

@bot.command()
async def chess(ctx):
    await ctx.send("Start a Chess game here: [link to a chess website or client]")

@bot.command()
async def playmusic(ctx, *, song):
    # Get the voice channel the user is in
    user_voice_channel = ctx.author.voice.channel if ctx.author.voice else None
    if user_voice_channel:
        music_bot_channel = bot.get_channel(music_bot_channel_id)
        if music_bot_channel:
            await ctx.send(f"Playing {song} in {user_voice_channel.name}...")
            # Tell the music bot to join the voice channel and play the song
            await music_bot_channel.send(f"-join {user_voice_channel.name}")
            await music_bot_channel.send(f"-play {song}")
        else:
            await ctx.send("Music channel not found. Double-check the channel ID.")
    else:
        await ctx.send("You need to be in a voice channel to play music.")

@bot.command()
async def stopmusic(ctx):
    music_bot_channel = bot.get_channel(music_bot_channel_id)
    if music_bot_channel:
        await ctx.send("Stopping the music...")
        await music_bot_channel.send("-stop")
    else:
        await ctx.send("Music channel not found. Double-check the channel ID.")

@bot.command()
async def pausemusic(ctx):
    music_bot_channel = bot.get_channel(music_bot_channel_id)
    if music_bot_channel:
      await music_bot_channel.send("-pause")
    else:
        await ctx.send("Music channel not found. Double-check the channel ID.")

@bot.command()
async def resumemusic(ctx):
    music_bot_channel = bot.get_channel(music_bot_channel_id)
    if music_bot_channel:
      await music_bot_channel.send("-resume")
    else:
        await ctx.send("Music channel not found. Double-check the channel ID.")

bot.run(TOKEN)