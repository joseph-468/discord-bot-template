import os
import discord
from discord import Intents
from discord.ext import commands
from dotenv import load_dotenv

# Setup
activity = discord.Activity(type=discord.ActivityType.listening, name="!help")
intents = Intents.all()
client = commands.Bot(command_prefix="!", help_command=None, intents=intents, activity=activity)


# Commands
@client.command()
async def ping(ctx):
    await ctx.send(f"Ping: {round(client.latency * 1000)}")


# Import token from env file and run the bot
if __name__ == "__main__":
    load_dotenv()
    client.run(os.getenv("TOKEN"))
