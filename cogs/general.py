import discord
from discord.ext import commands  # Yep, you need to import this again.

class General(commands.Cog):  # The cog is a class.
  def __init__(self, client):  # Sets a couple of basic variables, doesn't do much but it's pretty important.
    self.bot = client
    self._last_member = None
    
  @commands.command()  # Finally, we get to actually making a command.
  async def ping(self, ctx):  # All commands must be defined as asynchronous, and in cogs must have "self" as the 1st argument. ctx is required if you want to use the bot's functions.
    latency = round(self.bot.latency * 1000)  # Returns the bot's latency in milliseconds.
    await ctx.send("Pong! Latency is {}ms.".format(latency))  # ctx.send(text) sends a message as the bot. It must be ran asynchronously, as do all commands that use the bot's functions. (ctx commands and such)
    
  def setup(client):  # This is required.
    client.add_cog(General(client))
