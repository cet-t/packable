import discord
from discord.ext import commands as cmd

import os

intents = discord.Intents.all()
bot = cmd.Bot(command_prefix='>', intents=intents)


@bot.command()
async def ping(m):
    await m.send('pong')

async def help(m) -> None:
    await m.send('pong')

token = os.environ("TOKEN")
bot.run(token)
