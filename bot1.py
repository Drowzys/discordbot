import discord
from discord.ext.commands import Bot
from discord.ext import commands

Client = discrod.Client()
bot_prefix= "."
client = commands.Bot(command_prefix=bot_prefix)


@client.event
async def on_ready():
	print(Bot Online!)
	print(Name {}).format(client.user.name)
	pritn(ID: {}).format(client.user.id)

@client.command(pass_context=True)
async def ping():
	await client.say("Pong!")


client.run('MzQ0NjE5MTk5OTk1NDQ1MjU5.DHAfKA.o1t935Ij4AkIIDpPNXktrzexQYI')
