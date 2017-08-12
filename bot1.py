import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands

client = discord.Client()
bot_prefix= "."
client = commands.Bot(command_prefix=bot_prefix)


@client.event
async def on_ready():
    print("Bot Online!")
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))

@client.command(pass_context=True)
async def ping(ctx):
	await client.say("Pong!")


@client.command(pass_context=True)
async def connect(ctx):
    if client.is_voice_connected(ctx.message.server):
        return await client.say("I am already connected to a voice channel. Do not disconnect me if I am in use!")
    author = ctx.message.author
    voice_channel = author.voice_channel
    vc = await client.join_voice_channel(voice_channel)

@client.command(pass_context = True)
async def disconnect(ctx):
    for x in client.voice_clients:
        if(x.server == ctx.message.server):
            return await x.disconnect()	



client.run('MzQ0NjE5MTk5OTk1NDQ1MjU5.DHAfKA.o1t935Ij4AkIIDpPNXktrzexQYI')
