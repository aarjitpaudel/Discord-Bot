import discord
import asyncio
import json
import os
from webserver import keep_alive
from discord.ext import commands, tasks
from itertools import *
import random
import aiohttp
import string
from discord.utils import find

class events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.sniped_messages = {}

    
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        self.bot.sniped_messages[message.guild.id] = message


    @commands.command()
    async def snipe(self, ctx):
        try:
            snipemsg = self.bot.sniped_messages[ctx.guild.id]  # just take message
        
        except:
            await ctx.channel.send("Couldn't find a message to snipe!")
            return

        embed = discord.Embed(description=snipemsg.content, color=discord.Color.purple(), timestamp=snipemsg.created_at)
        embed.set_author(name=f"Message Was Sent By {snipemsg.author}", icon_url=snipemsg.author.avatar_url)
        embed.set_footer(text=f"Deleted in : #{snipemsg.channel.name}")


        await ctx.channel.send(embed=embed)








def setup(bot): 
  bot.add_cog(events(bot))