from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['NjMwMTY5MzUyNjQwOTIxNjQw.XZlCMg.ri8CRZSSe13qpRwrBuzXEseQJk4']


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


bot.run('NjMwMTY5MzUyNjQwOTIxNjQw.XZlCMg.ri8CRZSSe13qpRwrBuzXEseQJk4')
