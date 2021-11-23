import os
import pickle

import discord
from discord.ext import commands

import encrypt
from DiscordBot.logs import Logs

token = encrypt.decrypt(pickle.load(open("./config/token.idd", "rb")), encrypt.read_private_key("./keys/private_key.pem")).decode()

logs = Logs()

logs.writeline("\n")
logs.writeline("Script initialized.")

client = commands.Bot(command_prefix="-")
print("Bot initialized.")
logs.writeline("Bot initialized.")


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.do_not_disturb)


@client.event
async def on_member_join(member):
    pass


@client.command()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")


for filename in os.listdir(f"./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")


client.run(token)
logs.writeline("Client running.\n")
