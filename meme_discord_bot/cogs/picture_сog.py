import os
import discord
from discord.ext import commands, tasks
from discord.utils import get
import random

class PictureCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.picture_dir = "..\\images"
        self.send_picture.start()

    def cog_unload(self):
        self.send_picture.cancel()

    @tasks.loop(minutes=15)
    async def send_picture(self):
        for channel in self.bot.get_all_channels():
            if isinstance(channel, discord.TextChannel) and channel.permissions_for(channel.guild.me).send_messages:
                pictures = os.listdir(self.picture_dir)
                picture = random.choice(pictures)
                with open(f"{self.picture_dir}/{picture}", "rb") as fp:
                    await channel.send(file=discord.File(fp))

    @send_picture.before_loop
    async def before_send_picture(self):
        await self.bot.wait_until_ready()

async def setup(bot):
    await bot.add_cog(PictureCog(bot))
