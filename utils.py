from discord.ext import commands
from env import activity_channel_id, fallout_channel_id


async def sendActivityMessage(bot: commands.Bot, message: str):
    activity_channel = bot.get_channel(activity_channel_id)
    await activity_channel.send(message)


async def sendFalloutMessage(bot: commands.Bot, message: str | Exception):
    fallout_channel = bot.get_channel(fallout_channel_id)
    await fallout_channel.send(message)
