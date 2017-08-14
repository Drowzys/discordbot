import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import random
import namegen
from namegen import name
from namegen import race
from namegen import age
from namegen import char
 
#what you put before the command
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
        return await client.say("Already connected !")
    author = ctx.message.author
    voice_channel = author.voice_channel
    vc = await client.join_voice_channel(voice_channel)

@client.command(pass_context = True)
async def disconnect(ctx):
    for x in client.voice_clients:
        if(x.server == ctx.message.server):
            return await x.disconnect()	

@client.command(pass_context=True)
async def roleplay(ctx):
    name()
    char()
    age()
    race()

    await client.say("Your role is {}, you are {} years old, you are {} and you are {}!".format(name(), age(), char(), race()))

@client.command(pass_context=True)       
async def clear(ctx, number):
    mgs = []
    number = int(number) 
    async for x in client.logs_from(ctx.message.channel, limit = number):
        mgs.append(x)
    await client.delete_messages(mgs)


@client.command(pass_context=True)
async def rape(ctx, args):
	await client.say("You raped {}".format(args))

    

client.run('MzQ0NjE5MTk5OTk1NDQ1MjU5.DHAfKA.o1t935Ij4AkIIDpPNXktrzexQYI')
