from discord_slash import SlashContext
import discord


class Suggestion:

    @staticmethod
    async def create(ctx: SlashContext, channel:discord.channel.TextChannel, text):
        if channel.category_id is None:
            return False

        embed = discord.Embed()
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
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

        embed.description = text
        await msg.edit(embed=embed)
        await ctx.send(hidden=True, content='Suggestion modified!')
