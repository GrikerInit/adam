import discord
from discord.ext import commands
import os
 
client = discord.Client()
token = os.getenv("DISCORD_BOT_TOKEN")

@client.event
async def on_ready():
 print('Bot is ready')

hi = "Hi son"
weather = "How is the weather"

@client.event
async def on_message(message):
    if message.content == hi:
        await message.channel.send('hello daddy :smile:')

@client.event
async def on_message(message):
    if message.content == weather:
        await message.channel.send('Weather is Good')

@client.event
async def on_message(message):
    if message.content == "test":
        await message.channel.send('I work now')

client.run(token)