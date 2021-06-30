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
    if message.content == "Hi son":
        await message.channel.send('Hi daddy :smile:')

@client.event
async def on_message(message1):
    if message1.content == "How is the weather":
        await message1.channel.send("The Weather is good today")
        
client.run(token)