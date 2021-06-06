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
        embed.set_author(name=ctx.author_id, icon_url=ctx.author.avatar_url)
        embed.description = text
        embed.color = discord.Colour.gold()
        msg:discord.Message = await channel.send(embed=embed)
        embed.set_footer(text='To modify use:  /edit channel:#'+channel.name+' suggestion_id:'+str(msg.id)+' text:new content')
        await msg.edit(embed=embed)
        await msg.add_reaction("👍")
        await msg.add_reaction("👎")
        await ctx.send(hidden=True, content='Thank you for your suggestion!')

    @staticmethod
    async def edit(ctx: SlashContext, channel:discord.channel.TextChannel, suggestion_id:int, text):
        try:
            msg:discord.Message = await channel.fetch_message(suggestion_id)
        except Exception:
            await ctx.send(hidden=True, content='Suggestion not found.')
            return False

        embed:discord.Embed = msg.embeds[0]

        if embed.color != discord.Colour.gold() or int(embed.author.name) != ctx.author_id:
            await ctx.send(hidden=True, content='You cannot modify this suggestion!')
            return False

        embed.description = text
        await msg.edit(embed=embed)
        await ctx.send(hidden=True, content='Suggestion modified!')

    @staticmethod
    async def approve(ctx: SlashContext, channel:discord.channel.TextChannel, suggestion_id:int):
        if ctx.author_id not in ADMINS:
            await ctx.send(hidden=True, content='Nope.')
            return False

        try:
            msg:discord.Message = await channel.fetch_message(suggestion_id)
        except Exception:
            await ctx.send(hidden=True, content='Suggestion not found.')
            return False

        embed:discord.Embed = msg.embeds[0]

        embed.color = discord.Colour.green()
        embed.set_footer(text='Suggestion Approved')
        await msg.edit(embed=embed)
        await ctx.send(hidden=True, content='Suggestion has been approved')

    @staticmethod
    async def refuse(ctx: SlashContext, channel:discord.channel.TextChannel, suggestion_id:int):
        if ctx.author_id not in ADMINS:
            await ctx.send(hidden=True, content='Nope.')
            return False

        try:
            msg:discord.Message = await channel.fetch_message(suggestion_id)
        except Exception:
            await ctx.send(hidden=True, content='Suggestion not found.')
            return False

        embed:discord.Embed = msg.embeds[0]
        embed.color = discord.Colour.red()
        embed.set_footer(text='Suggestion refused')
        await msg.edit(embed=embed)
        await ctx.send(hidden=True, content='Suggestion has been refused')

    @staticmethod
    async def purge_suggestions(ctx: SlashContext, channel:discord.channel.TextChannel, user_id:int):
        if ctx.author_id not in ADMINS:
            await ctx.send(hidden=True, content='Nope.')
            return False

        messages = []
        for msg in await channel.history():
            embed:discord.Embed = msg.embeds[0]
            if int(embed.author) == user_id:
                messages.append(msg)

        channel.delete_messages(messages=messages)
        await ctx.send(hidden=True, content='Suggestions removed')
    
    @staticmethod
    async def purge_messages(ctx: SlashContext, channel:discord.channel.TextChannel, user_id:int):
        if ctx.author_id not in ADMINS:
            await ctx.send(hidden=True, content='Nope.')
            return False

        messages = []
        for msg in await channel.history():
            if msg.author_id == user_id:
                messages.append(msg)

        channel.delete_messages(messages=messages)
        await ctx.send(hidden=True, content='Messages removed')
        
        
        