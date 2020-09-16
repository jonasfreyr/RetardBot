import discord
from discord.ext import commands
from key import token_key

client = commands.Bot(command_prefix = '.')

retards = []

@client.event
async def on_ready():
    print("Retard ready")

@client.command()
async def addRetard(ctx, clientuser):
    retards.append(clientuser)

    await ctx.send(f"Retard {clientuser} added!")

@client.command()
async def checkRetards(ctx):
    string = "Retards:\n"
    for user in retards:
        string += str(user) + "\n"

    await ctx.send(string)

@client.command()
async def retard(ctx, message):
    await ctx.send(f"{message} is a retard")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.author.id in retards:
        await message.channel.send("Shut up retard!")

    await client.process_commands(message)


client.run(token_key)


