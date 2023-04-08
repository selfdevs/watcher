from discord.ext import commands
from helpers.env import activity_channel_id, fallout_channel_id
from json import dumps
from datetime import datetime

log_file = open("./data/log.jsonl", "a+")


async def sendActivityMessage(bot: commands.Bot, message: str):
    activity_channel = bot.get_channel(activity_channel_id)
    await activity_channel.send(message)


async def sendFalloutMessage(
    bot: commands.Bot, message: str | Exception, logMessage: str | None = None
):
    fallout_channel = bot.get_channel(fallout_channel_id)
    await fallout_channel.send(message)
    logEvent("coworking", logMessage or message, "")


def logEvent(event: str, message: str, member: str):
    log_file.write(
        dumps(
            {
                "timestamp": datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),
                "event": event,
                "message": message,
                "member": member,
            },
        )
        + "\n"
    )
