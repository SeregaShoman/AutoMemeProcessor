import discord
from .src.generate_msg import generate_msg_txt
from discord.ext import commands

class EventCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):    
        if message.author == self.bot.user:
            return
        if message.content.startswith(self.bot.command_prefix) == True:
            return
        if isinstance(message.channel, discord.TextChannel) and message.content == "Привет":
            channel = message.channel
            await channel.send(generate_msg_txt())
        await self.bot.process_commands(message)

async def setup(bot):
    await bot.add_cog(EventCog(bot))