import asyncio
import typing
from typing import Any

import discord
from discord.ext import commands


intents = discord.Intents.all()
bot = commands.Bot(command_prefix='>', intents=intents)


@bot.command()
async def ping(m):
    await m.send('pong')


async def help(m) -> None:
    await m.send('pong')

if __name__ == "__main__":
    import os
    import pathlib

    import discord
    from dotenv import load_dotenv

    load_dotenv()

    file = pathlib.Path(__file__).resolve()
    prefix = file.parent
    ERROR = "STOP"

    try:
        token = os.environ["token"]
    except KeyError:
        token = ERROR

    intents = discord.Intents.all()

    class MyBot(commands.Bot):
        async def on_ready(self) -> None:
            print("ready")

        async def setup_hook(self) -> None:
            await self.load_extension(file.stem)
            try:
                guild_id =
            except KeyError:
                guild_id = ERROR

            guild = self.get_guild(guild_id)
            if guild is None:
                guild = await self.fetch_guild(guild_id)

            self.tree.copy_global_to(guild=guild)
            await self.tree.sync(guild=guild)
            await self.tree.sync()

    bot = MyBot("t!", intents=intents)
    bot.run(token)
