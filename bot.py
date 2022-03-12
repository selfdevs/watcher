from os import environ, listdir
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

token = environ['DISCORD_TOKEN']

bot = commands.Bot(command_prefix='>', help_command=None)

@bot.event
async def on_ready():
  print("====================")
  print("self.dev Watcher is ready")
  print("====================")

for filename in listdir('./events'):
    if filename.endswith('.py'):
        bot.load_extension(f'events.{filename[:-3]}')

bot.run(token)
