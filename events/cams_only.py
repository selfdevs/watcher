from discord.ext import commands
from discord import Member, VoiceState
from discord.channel import VocalGuildChannel
from asyncio import sleep
from helpers.utils import sendActivityMessage, sendFalloutMessage, logEvent, keep_letters_only
from helpers.env import (
    cam_only_channel_ids,
    cams_only_warn_period,
    cams_only_kick_period,
    cams_only_warn_period_nextlevel,
    cams_only_kick_period_nextlevel,
    cams_only_move_vc_id,
    role_nextlevel
)

member_register: dict[int, Member] = {}


async def start_warn_procedure(
    bot: commands.Bot, channel: VocalGuildChannel, member: Member
):
    NL_members = [850234321074651167, 473190806086221825, 520317475733372941,
            280461648865525761, 280461648865525761] # alex, long, mvx, blazer, 10act
    if member.id in NL_members :
        print("An ENFORCER joined the channel. They are immune!")
#    if str(role_nextlevel) in [str(role.name) for role in member.roles]:
        warn_period = cams_only_warn_period_nextlevel
        kick_period = cams_only_kick_period_nextlevel
    else:
        print(f"User does not have the role: {role_nextlevel}")
        warn_period = cams_only_warn_period
        kick_period = cams_only_kick_period

    await sleep(warn_period)

    if not member_register[member.id].voice.channel.id in cam_only_channel_ids:
        return
    await sendActivityMessage(
        bot, f"Started cam-only warn procedure on: {member.name}#{member.discriminator}"
    )
    logEvent(
        "cams-only",
        "Started cam-only warn procedure",
        f"{member.name}#{member.discriminator}",
    )
    if (
        member_register[member.id].voice
        and not member_register[member.id].voice.self_video
        and member_register[member.id].voice.channel.id in cam_only_channel_ids
    ):
        await channel.send(
            f"{member.mention}, You've been warned! This is a cam-only channel, turn on your cam in {cams_only_kick_period} seconds or you'll be kicked out of VC"
        )
        await sleep(kick_period)
        if (
            member_register[member.id].voice
            and not member_register[member.id].voice.self_video
            and member_register[member.id].voice.channel.id in cam_only_channel_ids
        ):
            await member.move_to(bot.get_channel(cams_only_move_vc_id))
            await channel.send(
                f"kicked {member.mention} because they didn't turn on their cam.",
                silent=True,
            )
            await sendActivityMessage(
                bot,
                f"Finished cam-only warn procedure on: {member.name}#{member.discriminator}",
            )
            logEvent(
                "cams-only",
                "Finished cam-only warn procedure on",
                f"{member.name}#{member.discriminator}",
            )
        else:
            await sendActivityMessage(
                bot,
                f"Aborted cam-only warn procedure on: {member.name}#{member.discriminator}",
            )
            logEvent(
                "cams-only",
                "Aborted cam-only warn procedure on",
                f"{member.name}#{member.discriminator}",
            )
    else:
        await sendActivityMessage(
            bot,
            f"Aborted cam-only warn procedure on: {member.name}#{member.discriminator}",
        )
        logEvent(
            "cams-only",
            "Aborted cam-only warn procedure on",
            f"{member.name}#{member.discriminator}",
        )


class cams_only(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        print("Cams only cog loaded!")

    @commands.Cog.listener()
    async def on_voice_state_update(
        self,
        member: Member,
        _,
        after: VoiceState,
    ):
        try:
            if after.channel and after.channel.id in cam_only_channel_ids:
                member_register[member.id] = member
                if not member.voice.self_video:
                    await start_warn_procedure(self.bot, after.channel, member)
        except Exception as e:
            await sendFalloutMessage(self.bot, e)


async def setup(bot):
    await bot.add_cog(cams_only(bot))

