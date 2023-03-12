import discord
import tensorflow as tf
from .src.generate_msg import generate_msg_txt
from discord.ext import commands
from .intent_classification.analyse_words_process import voice_tag

greetings = tf.saved_model.load('..\\models\\greetings')
endings = tf.saved_model.load('..\\models\\endings')

class EventCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):    
        scores = voice_tag(message.content)
        print(scores, type(scores[0]))
        if message.author == self.bot.user:
            return
        if message.content.startswith(self.bot.command_prefix) == True:
            return
        if isinstance(message.channel, discord.TextChannel):
            channel = message.channel
            if'GREETINGS' in scores:
                text = generate_msg_txt(greetings)
            elif 'ENDING' in scores:
                text = generate_msg_txt(endings)
            else:
                return
        await channel.send(text)
        await self.bot.process_commands(message)

async def setup(bot):
    await bot.add_cog(EventCog(bot))