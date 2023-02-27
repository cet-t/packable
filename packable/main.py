import discord
from discord.ext import commands
from discord_slash import SlashCommand

import json
import typing

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='pack ', intents=intents)
slash = SlashCommand(bot, sync_command=True)

dice_name: str
dice_crew: str
dice_crit: int


class DicerDict:
    infos_path = './info.json'

    def __init__(self, ign: str, joined_crew: str, crit_damage: int) -> None:
        self.name = ign
        self.crew = joined_crew
        self.crit = crit_damage

    def to_dict(self) -> dict[str, typing.Any]:
        info: dict[str, typing.Any] = {
            'name': self.name,
            'crew': self.crew,
            'crit': self.crit
        }
        return info

    def write_json(self, info_data: dict[str, typing.Any]):
        with open(self.infos_path, 'w') as f:
            json.dump(info_data, f)


def read_json(ign: str):
    with open(DicerDict.infos_path) as f:
        load_info = json.load(f)
        return load_info


@bot.command()
async def add(ctx):
    await ctx.reply('準備中')


@bot.command()
async def test(ctx):  # ? $test で呼び出し
    await ctx.send('send')
    await ctx.reply('reply')


if __name__ == "__main__":
    import os
    from dotenv import load_dotenv
    load_dotenv()

    token = os.environ["TOKEN"]

    @bot.event
    async def on_ready():
        print(f"{bot.user} is ready")

    bot.run(token)
