from discord_slash import SlashContext
import discord
from settings import *

class Suggestion:

    @staticmethod
    async def create(ctx: SlashContext, channel:discord.channel.TextChannel, text):
        if channel.id not in CATEGORIES:
            await ctx.send(hidden=True, content='You cannot send a message in this category!')
            return False

        embed = discord.Embed()
        embed.set_author(name=ctx.author.id, icon_url=ctx.author.avatar_url)
        embed.description = text
        embed.color = discord.Colour.gold()
        msg:discord.Message = await channel.send(embed=embed)
        embed.set_footer(text='To modify use:  /edit channel:#'+channel.name+' suggestion_id:'+str(msg.id)+' text:new content')
        await msg.edit(embed=embed)
        await ctx.send(hidden=True, content='Thank you for your suggestion!')

    @staticmethod
    async def edit(ctx: SlashContext, channel:discord.channel.TextChannel, suggestion_id:int, text):
        msg:discord.Message = await channel.fetch_message(suggestion_id)
        embed:discord.Embed = msg.embeds[0]

        if embed.color == discord.Colour.green() or embed.color == discord.Colour.red() or int(embed.author.name) != ctx.author.id:
            await ctx.send(hidden=True, content='You cannot modify this suggestion!')
            return False

        embed.description = text
        await msg.edit(embed=embed)
        await ctx.send(hidden=True, content='Suggestion modified!')

    @staticmethod
    async def approve(ctx: SlashContext, channel:discord.channel.TextChannel, suggestion_id:int):
        if ctx.author_id is not ADMIN:
            await ctx.send(hidden=True, content='Nope.')
            return False

        msg:discord.Message = await channel.fetch_message(suggestion_id)
        embed:discord.Embed = msg.embeds[0]

        embed.color = discord.Colour.green()
        embed.set_footer(text='Suggestion Approved')
        await msg.edit(embed=embed)
        await ctx.send(hidden=True, content='Suggestion has been approved')
