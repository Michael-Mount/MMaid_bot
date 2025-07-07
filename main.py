import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import random

## Loads the current enviroment file content
load_dotenv()
token = os.getenv('DISCORD_TOKEN')

if not token:
    raise ValueError("DISCORD_TOKEN isn't being passed form .env or is empty")

## Log of errors and events
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

## The list of intents the Discord bot has from Discord App
intents = discord.Intents.default()

intents.message_content = True
intents.members = True

## Command Prefic trigger
bot = commands.Bot(command_prefix='!', intents=intents)

## Basic Event to confrim Bot has connected to server
@bot.event
async def on_ready():
    print(f"Howdy, {bot.user.name} is live!")

## Start Command
bot.run(token, log_handler=handler, log_level=logging.DEBUG)