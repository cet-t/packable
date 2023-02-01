import discord
from discord.ext import commands as cmd

import os

intents = discord.Intents.all()
bot = cmd.Bot(command_prefix='>', intents=intents)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

token = os.environ("TOKEN")
bot.run(token)
