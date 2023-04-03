from os import listdir
from discord.ext import commands
from discord import Intents
from helpers.utils import sendFalloutMessage
import asyncio

from helpers.env import (
    coworking_channel_ids,
    coworking_role_id,
    cam_only_channel_ids,
    cams_only_kick_period,
    cams_only_warn_period,
    discord_token,
    activity_channel_id,
)

intents = Intents.default()
intents.voice_states = True
intents.message_content = True

bot = commands.Bot(command_prefix=">", help_command=None, intents=intents)


def printVoiceChannels(channel_ids_list: list[int]):
    message = ""
    for i, channel_id in enumerate(channel_ids_list):
        channel = bot.get_channel(channel_id)
        message += f"`{i+1}. {channel.name}`\n"
    return message


@bot.event
async def on_ready():
    print("====================")
    print("self.dev Watcher is ready")
    print("====================")
    await sendFalloutMessage(
        bot,
        f"""```Initializing watcher, make sure that the bot is put above the coworking role to avoid any issues ```
        **Current watcher configuration**

        **Co-working VCs**
        {printVoiceChannels(coworking_channel_ids)}
        *Co-working role ID*
        {coworking_role_id}

        **Cam-only VCs**
        {printVoiceChannels(cam_only_channel_ids)}
        - Warn period: {cams_only_warn_period} seconds
        - Kick period: {cams_only_kick_period} seconds

        **Activity Channel**
        {bot.get_channel(activity_channel_id).mention}
        
        All the issues will be reported in this channel.
        
        Alright bye now, time to watch :nazar_amulet:
        """,
    )


async def loadCogs():
    for filename in listdir("./events"):
        if filename.endswith(".py"):
            await bot.load_extension(f"events.{filename[:-3]}")


asyncio.run(loadCogs())

bot.run(discord_token)
