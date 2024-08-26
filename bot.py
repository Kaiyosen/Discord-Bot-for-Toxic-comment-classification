import discord
from discord.ext import commands
import random
import os
client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('REM is ready.')

@client.command(description = 'Clear the messages with .clear {} where {} is number of messages you want to delete')
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit = amount)

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please pass in the amount of messages to delete.')

@client.command(description = 'As the name suggests, I will load the desired cog for you.')
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} cog is loaded successfully!')

@client.command(description = 'As the name suggests, I will UNload the desired cog for you.')
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} cog is unloaded successfully!')

@client.command(description = 'I will UNload and then load the desired cog for you.')
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} cog is reloaded successfully!')

@client.command
async def DM(ctx):
    await ctx.author.send("Hello this is your direct convo with Rem-Chan")

for filename in os.getcwd():
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        
        

client.run("OTY2NzMzOTEzODczNjAwNTk1.YmGDHg.WxKTS6VsjQ2jUwVvWe0KW2yZ6PA")