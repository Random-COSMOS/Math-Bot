import os
import discord
from dotenv import load_dotenv

client = discord.Client()
load_dotenv()

TOKEN = os.environ.get("TOKEN")

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(msg):
    if msg.author == client.user:
        return
    
    if msg.content.startswith("="):
        res = eval(msg.content[1:])
        await msg.channel.send(str(res))

client.run(TOKEN)