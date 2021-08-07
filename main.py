token = ""  # Your Discord bot token goes in here.

import time
timerStart = time.time()  # This is used for showing how long the bot took to load.

import discord
from discord.ext import commands  # Basically imports everything you need in this file. (the main one, commands will be written in cogs)

client = commands.Bot(command_prefix="!")  # This is the bot object. Definitely change the command prefix.

extensions = ["cogs.general", "jishaku"]  # Put your cogs in here using the formatting displayed here (imports the cog in cogs/general.py). Jishaku allows you to execute code from your own account, check the bot's status, debug errors and more.

for extension in extensions:  # This loads all the extensions in the list. (if for some reason you don't know how for loops work)
  try:
    print('Attempting to load extension "{}"'.format(extension))
    client.load_extension(extension)  # This is the function to load an extension / cog.
  except Exception as e:
    print('Failed to load extension "{}" ({})'.format(extension, e))  # Pretty self explanatory.
    
@client.event
async def on_ready():
  sec = round(time.time() - timerStart, 4)  # How long the bot took to load.
  print("Bot loaded in {} seconds.".format(sec))
  
print("Starting bot...")
client.run(token)  # Actually runs the bot. Nothing can be ran after this in the file, hence the on_ready() function.
