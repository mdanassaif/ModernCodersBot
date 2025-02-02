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
    music_bot_channel = bot.get_channel(music_bot_channel_id)
    if music_bot_channel:
        await ctx.send(f"Playing {song}...")
        await music_bot_channel.send(f"-play {song}")
    else:
        await ctx.send("Music channel not found. Double-check the channel ID.")

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