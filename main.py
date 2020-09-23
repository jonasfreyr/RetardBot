import discord
import json
from discord.ext import commands
from key import token_key

client = commands.Bot(command_prefix = '.')

retards = []

def saveRetards():
    with open("retards.json", 'w') as file:
        json.dump(retards, file)

def loadRetards():
    try:
        with open("retards.json", 'r') as file:
            retards = json.load(file)
    except:
        print("Failed to read retards.json")

@client.event
async def on_ready():
    loadRetards()
    print("Retard ready")

@client.command()
async def addRetard(ctx):
    message = ctx.message
    string = "Retards Added:\n"

    for mention in retards:
        if mention == ctx.author.mention:
            await ctx.send("Nice try retard")
            return

    if client.user in message.mentions:
        await ctx.send("Nice try retard")
        return

    for user in message.mentions:
        retards.append(user.mention)
        string += str(user.mention) + "\n"
    
    saveRetards()

    await ctx.send(string)

@client.command()
async def removeRetard(ctx):
    message = ctx.message
    string = "Retards Removed:\n"

    for mention in retards:
        for user in message.mentions:
            if mention == user.mention:
                await ctx.send("Nice try retard")
                return

    for user in message.mentions:
        retards.remove(user.mention)

        string += str(user.mention) + "\n"

    saveRetards()

    await ctx.send(string)

@client.command()
async def clearRetards(ctx):
    global retards
    for mention in retards:
        if mention == ctx.author.mention:
            await ctx.send("Nice try retard")
            return

    retards = []
    saveRetards()
    
    await ctx.send("Retards cleared")

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

    if message.author.mention in retards:
        await message.channel.send("Shut up retard!")

    await client.process_commands(message)


client.run(token_key)


