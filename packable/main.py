# packable
import discord
import asyncio
import os
import keep_alive
import random as r
import sys
from datetime import datetime as date
import nutslist as n
import almostenv as env
import time

# py D:\desktop\packable\main.py
os.system("pip install -U git+https://github.com/Rapptz/discord.py")

sys.path.append("nutslist.py")
sys.path.append("almostenv.py")
t = str.format(env.token)

intents = discord.Intents.all()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(client.user.name, 'is login')


@client.event
async def on_delete_message(m):
    user = m.author
    uid = m.author.id
    msg = m.content
    tid = m.content.id
    await m.channel.send(f"name: {user}\nuserid: {uid}\nmessage: {msg}\nmid: {tid}")


@client.event
async def on_message(m):
    if m.author.bot:
        return

    elif m.content == "いま":
        now = date.now().strftime("%Y%m%d%h%m%s")
        await m.channel.send(now)

    elif m.content.startswith("p"):
        un = m.content 			# "p cet"
        uname = un.split(' ')  # ["p", "cet"]
        dicer = uname[1]
        n.nuts.append(dicer)
        (un, uname) = (None, None)
        await m.channel.send("done")

    elif m.content == "p list":
        j = len(n.nuts)
        for i in range(j):
            await m.channel.send(n.nuts[i])

client.run(t)

'''
https://note.nkmk.me/python-split-rsplit-splitlines-re/
'''

'''
import discord
import asyncio
import os
import keep_alive
import random as r
import nutslist
import sys

sys.path.append("/home/runner/nutslist.py")

os.system("pip install -U git+https://github.com/Rapptz/discord.py")

client = discord.Client()

token = 'NzMyOTQwNDk5MDIzMDM2NTI4.Xw76CA.3xY-YH2YQrA6UivzEsiw1IEoK_Q'


@client.event
async def on_ready():
	print(client.user.name, 'is login')

@client.event
async def on_message(m):

	if m.author.bot:
		return

	elif m.content


keep_alive.keep_alive()
client.run(os.getenv('token'))
'''
