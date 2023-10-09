import nextcord
import os
from nextcord.ext import commands

from dotenv import load_dotenv

intents = nextcord.Intents.all()

load_dotenv()

token = os.getenv('TOKEN')
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(token)
