import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.command()
async def test(ctx):
    await ctx.send("test sent")


if __name__ == "__main__":
    import os
    import pathlib

    import discord
    from dotenv import load_dotenv

    load_dotenv()

    file = pathlib.Path(__file__)

    try:
        token = os.environ["TOKEN"]
    except KeyError:
        token = os.environ["ERROR"]

    @bot.event
    async def on_ready():
        print(f"{bot.user} is ready")

    bot.run(token)
