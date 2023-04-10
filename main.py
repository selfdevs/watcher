from os import listdir
from discord.ext import commands
from discord import Intents
from helpers.utils import sendFalloutMessage, log_file
import asyncio
import helpers.env as env


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
    print("activity_channel_id=", env.activity_channel_id)
    print("cam_only_channel_ids=", env.cam_only_channel_ids)
    print("cams_only_kick_period=", env.cams_only_kick_period)
    print("cams_only_move_vc_id=", env.cams_only_move_vc_id)
    print("cams_only_warn_period=", env.cams_only_warn_period)
    print("coworking_channel_ids=", env.coworking_channel_ids)
    print("coworking_role_id=", env.coworking_role_id)
    print("discord_token=", env.discord_token)
    print("fallout_channel_id=", env.fallout_channel_id)

    print("====================")
    print("self.dev Watcher is ready")
    print("====================")
    await sendFalloutMessage(
        bot,
        f"```Initializing watcher, make sure that the bot is put above the coworking role to avoid any issues ```"
        + "\n**Current watcher configuration**\n"
        + f"\n**Co-working VCs**\n{printVoiceChannels(env.coworking_channel_ids)}\n*Co-working role ID*\n{env.coworking_role_id}\n"
        + f"\n**Cam-only VCs**\n{printVoiceChannels(env.cam_only_channel_ids)}\n- Warn period: {env.cams_only_warn_period} seconds\n- Kick period: {env.cams_only_kick_period} seconds\n"
        + "\n- Move VC: "
        + (
            bot.get_channel(env.cams_only_move_vc_id)
            and bot.get_channel(env.cams_only_move_vc_id).name
            or 'They gon" get kicked.'
        )
        + f"\n\n**Activity**\n\n{bot.get_channel(env.activity_channel_id).mention}"
        + "\nAll the issues will be reported in this channel.\n\nAlright bye now, time to watch :nazar_amulet:",
        "Initialized",
    )


async def loadCogs():
    for filename in listdir("./events"):
        if filename.endswith(".py"):
            await bot.load_extension(f"events.{filename[:-3]}")


asyncio.run(loadCogs())

bot.run(env.discord_token)
