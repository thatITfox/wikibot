import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix='fox', help_command=None)

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run("bot id")
