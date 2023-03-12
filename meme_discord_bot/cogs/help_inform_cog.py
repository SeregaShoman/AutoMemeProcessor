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
        message = 'ПРИВЕТ Я БОТ И Я ЛЮБЛЮ ИГРАТЬ В ДОТУ И ТРОЛИТЬ АХАХАХАХАХХАХАХАХАХАХАХА \n ВЫ ВСЕ УЁБКИ ТУПЫЕ БЛЯТЬ А Я КРУТОЙ'
        embed = discord.Embed(title='Информация', description=message, color=discord.Color.blurple())
        await ctx.send(embed=embed)
        return

async def setup(bot):
    await bot.add_cog(HelpInformCog(bot))