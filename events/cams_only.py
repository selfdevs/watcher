from discord.ext import commands
from discord import Member, VoiceState
from discord.channel import VocalGuildChannel
from asyncio import sleep
from utils import sendActivityMessage, sendFalloutMessage
from env import cam_only_channel_ids, cams_only_warn_period, cams_only_kick_period

member_register: dict[int, Member] = {}


async def cam_only_event(bot: commands.Bot, channel: VocalGuildChannel, member: Member):
    await start_warn_procedure(bot, channel, member)


async def start_warn_procedure(
    bot: commands.Bot, channel: VocalGuildChannel, member: Member
):
    await sleep(cams_only_warn_period)
    await sendActivityMessage(
        bot, f"Started cam-only warn procedure on: {member.name}#{member.discriminator}"
    )
    if (
        member_register[member.id].voice
        and not member_register[member.id].voice.self_video
    ):
        await channel.send(
            f"{member.mention}, You are warned! This is a cam-only channel, turn on your cam in 60 seconds or you'll be kicked out of VC"
        )
        await sleep(cams_only_kick_period)
        if (
            member_register[member.id].voice
            and not member_register[member.id].voice.self_video
        ):
            await member.move_to(None)
            await channel.send(
                f"kicked {member.mention} because they didn't turn on their cam.",
                silent=True,
            )
            await sendActivityMessage(
                bot,
                f"Finished cam-only warn procedure on: {member.name}#{member.discriminator}",
            )
        else:
            await sendActivityMessage(
                bot,
                f"Aborted cam-only warn procedure on: {member.name}#{member.discriminator}",
            )
    else:
        await sendActivityMessage(
            bot,
            f"Aborted cam-only warn procedure on: {member.name}#{member.discriminator}",
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
