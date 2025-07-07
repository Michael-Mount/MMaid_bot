import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import random

## Loads the current enviroment file content
load_dotenv()
token = os.getenv('DISCORD_TOKEN')

print(f"{token}")