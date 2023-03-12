import discord
import tensorflow as tf
from src.generate_msg import generate_msg_txt
from discord.ext import commands
import configparser

config = configparser.ConfigParser()
config.read('..\\config.ini', encoding='utf-8')

bot = commands.Bot(command_prefix='$', intents=discord.Intents.all(), case_insensitive=True, help_command=None)

@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))

@bot.event
async def on_message(message):    
    if message.author == bot.user:
        return


    if isinstance(message.channel, discord.TextChannel) and message.content == "Привет":
        channel = message.channel
        await channel.send(generate_msg_txt())
        
    await bot.process_commands(message)

bot.run(config["DISCORDBOT"]["token"])