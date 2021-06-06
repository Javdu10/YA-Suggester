import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_option
from Suggestion import *
from settings import *


bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
slash = SlashCommand(bot, sync_commands=True)

@slash.slash(
    name="suggest",
    description="Creates a suggestion",
    options=[
        create_option(
            name="channel",
            description="Where to send the suggestion.",
            option_type=7,
            required=True
        ),
        create_option(
            name="text",
            description="The content of the suggestion.",
            option_type=3,
            required=True
        )
    ]
)
async def _suggest(ctx: SlashContext, channel:discord.channel.TextChannel, text):
    await Suggestion.create(ctx, channel, text)


@slash.slash(
    name="edit",
    description="Edits a suggestion",
    options=[
        create_option(
            name="channel",
            description="In which channel is the suggestion.",
            option_type=7,
            required=True
        ),
        create_option(
            name="suggestion_id",
            description="Message id of the suggestion.",
            option_type=3,
            required=True
        ),
        create_option(
            name="text",
            description="The new content of the suggestion.",
            option_type=3,
            required=True
        )
    ]
)
async def _edit(ctx: SlashContext, channel:discord.channel.TextChannel, suggestion_id:int, text):
    await Suggestion.edit(ctx, channel, suggestion_id, text)

@slash.slash(
    name="approve",
    description="Approves a suggestion",
    options=[
        create_option(
            name="channel",
            description="In which channel is the suggestion.",
            option_type=7,
            required=True
        ),
        create_option(
            name="suggestion_id",
            description="Message id of the suggestion.",
            option_type=3,
            required=True
        )
    ]
)
async def _approve(ctx: SlashContext, channel:discord.channel.TextChannel, suggestion_id:int):
    await Suggestion.approve(ctx, channel, suggestion_id)

@slash.slash(
    name="refuse",
    description="Refuses a suggestion",
    options=[
        create_option(
            name="channel",
            description="In which channel is the suggestion.",
            option_type=7,
            required=True
        ),
        create_option(
            name="suggestion_id",
            description="Message id of the suggestion.",
            option_type=3,
            required=True
        )
    ]
)
async def _refuse(ctx: SlashContext, channel:discord.channel.TextChannel, suggestion_id:int):
    await Suggestion.refuse(ctx, channel, suggestion_id)

@slash.slash(
    name="purge_suggestions",
    description="Purges suggestions of an user",
    options=[
        create_option(
            name="channel",
            description="Which channel to purge.",
            option_type=7,
            required=True
        ),
        create_option(
            name="user_id",
            description="ID of the user.",
            option_type=3,
            required=True
        )
    ]
)
async def _purge_suggestions(ctx: SlashContext, channel:discord.channel.TextChannel, user_id:int):
    await Suggestion.purge_suggestions(ctx, channel, user_id)

@slash.slash(
    name="purge_messages",
    description="Purges messages of an user",
    options=[
        create_option(
            name="channel",
            description="Which channel to purge.",
            option_type=7,
            required=True
        ),
        create_option(
            name="user_id",
            description="ID of the user.",
            option_type=3,
            required=True
        )
    ]
)
async def _purge_messages(ctx: SlashContext, channel:discord.channel.TextChannel, user_id:int):
    await Suggestion.purge_messages(ctx, channel, user_id)

bot.run(DISCORD_BOT_TOKEN)
