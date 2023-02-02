import asyncio
import typing
from typing import Any

import discord
from discord.ext import commands


intents = discord.Intents.all()
bot = commands.Bot(command_prefix='>', intents=intents)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

if __name__ == "__main__":
    import os
    from pathlib import Path

    import discord
    from dotenv import load_dotenv as denv

    denv()

    file = Path(__file__).resolve()
    prefix = file.parent
    # try:
    #     token = os.environ["token"]
    # except KeyError:
    #     token = os.environ["DIS_TEST_TOKEN"]

    intents = discord.Intents.all()

    class MyBot(commands.Bot):
        async def on_ready(self) -> None:
            print("ready")

        async def setup_hook(self) -> None:
            await self.load_extension(file.stem)
            guild_id = ID_HERE
            guild = self.get_guild(guild_id)
            if guild is None:
                guild = await self.fetch_guild(guild_id)

            self.tree.copy_global_to(guild=guild)
            await self.tree.sync(guild=guild)
            await self.tree.sync()

    bot = MyBot("t!", intents=intents)
    bot.run(token)
