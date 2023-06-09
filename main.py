import os
import discord
import asyncio
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='&', case_insensitive=False, intents=intents, status=discord.Status.online, help_command=None)


@bot.event
async def on_ready():
    print(f'目前登入身份：{bot.user}')
    print('------')


async def main():
    async with bot:
        for name in os.listdir('./cmds'):
            if name.endswith('.py'):
                await bot.load_extension(f'cmds.{name[:-3]}')
                print(name)
        await bot.start('Your Bot Token')

asyncio.run(main())

