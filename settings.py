import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

DISCORD_BOT_TOKEN = os.environ.get("DISCORD_BOT_TOKEN")
CATEGORIES = [int(category) for category in os.environ.get("CATEGORIES").split(',')]
ADMINS = [int(admin) for admin in os.environ.get("ADMINS").split(',')]
