import discord
from discord.ext import commands
import os
 
client = discord.Client()
token = os.getenv("DISCORD_BOT_TOKEN")

@client.event
async def on_ready():
 print('Bot is ready')

test = "Hi son"

weathertest = "How is the weather"

@client.event
async def on_message(message):
    if message.content == test:
        await message.channel.send('hello daddy :smile:')

@client.event
async def on_message(message):
    if message.content == weathertest:
        await message.channel.send('Weather is Good')

@client.event
async def on_message(message):
    if message.content == "test":
        await message.channel.send('I work now')

client.run(token)