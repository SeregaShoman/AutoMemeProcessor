import discord
from discord.ext import commands

class HelpInformCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='help', brief='Показывает список команд', aliases=['myhelp'])
    async def help_command(self, ctx):
        embed = discord.Embed(title='Список команд', description='Список доступных команд:', color=discord.Color.blurple())
        for command in self.bot.commands:
            embed.add_field(name=command.name, value=command.brief, inline=False)
        await ctx.send(embed=embed)
        return
    
    @commands.command(name='inform', brief='Выводит информационное сообщение')
    async def inform_command(self, ctx):
        message = 'Привет, меня зовут Егорик! Я новый бот и умею общаться с помощью Rnn нейронных моделей. К тому же, я умею отправлять разные мемы! В будущем я буду обладать множеством других функций, так что оставайтесь на связи и следите за моим развитием! А вы, кстати, все еще уёбки тупые, а я - крутой! Ахахахахахаха!'
        embed = discord.Embed(title='Информация', description=message, color=discord.Color.blurple())
        await ctx.send(embed=embed)
        return

async def setup(bot):
    await bot.add_cog(HelpInformCog(bot))