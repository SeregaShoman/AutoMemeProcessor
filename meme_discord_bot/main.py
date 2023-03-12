import discord
import tensorflow as tf
from discord.ext import commands
import configparser

config = configparser.ConfigParser()
config.read('..\\config.ini', encoding='utf-8')

bot = commands.Bot(command_prefix='$', intents=discord.Intents.all(), case_insensitive=True, help_command=None)

@bot.event
async def on_ready():
    await bot.load_extension("cogs.event_cog")
    await bot.load_extension("cogs.help_inform_cog")
    await bot.load_extension("cogs.picture_сog")
    print('Logged in as {0.user}'.format(bot))

bot.run(config["DISCORDBOT"]["token"])
