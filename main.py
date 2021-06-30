import discord
from discord.ext import commands
import os
 
client = discord.Client()
token = os.getenv("DISCORD_BOT_TOKEN")

@client.event
async def on_ready():
 print('Bot is ready')

@client.event
async def on_message(message):
    if message.content.lower() == "hi son":
        await message.channel.send("hello daddy :smile:")
    elif message.content.lower() == "how is the weather":
        await message.channel.send('Weather is Good')
    else:
        pass

client.run(token)