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
    cams_only_move_vc_id,
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
        f"```Initializing watcher, make sure that the bot is put above the coworking role to avoid any issues ```"
        + "\n**Current watcher configuration**\n"
        + f"\n**Co-working VCs**\n{printVoiceChannels(coworking_channel_ids)}\n*Co-working role ID*\n{coworking_role_id}\n"
        + f"\n**Cam-only VCs**\n{printVoiceChannels(cam_only_channel_ids)}\n- Warn period: {cams_only_warn_period} seconds\n- Kick period: {cams_only_kick_period} seconds\n"
        + "\n- Move VC: "
        + (
            bot.get_channel(cams_only_move_vc_id)
            and bot.get_channel(cams_only_move_vc_id).name
            or 'They gon" get kicked.'
        )
        + f"\n\n**Activity**\n\n{bot.get_channel(activity_channel_id).mention}"
        + "\nAll the issues will be reported in this channel.\n\nAlright bye now, time to watch :nazar_amulet:",
        "Initialized",
    )


async def loadCogs():
    for filename in listdir("./events"):
        if filename.endswith(".py"):
            await bot.load_extension(f"events.{filename[:-3]}")


asyncio.run(loadCogs())

bot.run(discord_token)
