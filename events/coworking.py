from discord.ext import commands
from discord import Member, VoiceState
from helpers.env import coworking_role_id, coworking_channel_ids
from helpers.utils import sendActivityMessage, sendFalloutMessage, logEvent


class coworking(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        print("Co-working cog loaded!")

    @commands.Cog.listener()
    async def on_voice_state_update(
        self,
        member: Member,
        before: VoiceState,
        after: VoiceState,
    ):
        try:
            guild = self.bot.get_guild(member.guild.id)
            role = guild.get_role(coworking_role_id)
            before_channel = before.channel
            after_channel = after.channel

            if (
                after_channel
                and after_channel.id in coworking_channel_ids
                and before_channel
                and before_channel.id in coworking_channel_ids
            ):
                if role not in member.roles:
                    await member.add_roles(role, reason="Joined Co-working vc")
                await sendActivityMessage(
                    self.bot,
                    f"{member.name}#{member.discriminator} left {before_channel.name}",
                )
                logEvent(
                    "coworking",
                    f"left {before_channel.name}",
                    f"{member.name}#{member.discriminator}",
                )
                await sendActivityMessage(
                    self.bot,
                    f"{member.name}#{member.discriminator} joined {after_channel.name}",
                )
                logEvent(
                    "coworking",
                    f"joined {after_channel.name}",
                    f"{member.name}#{member.discriminator}",
                )
            elif after_channel and after_channel.id in coworking_channel_ids:
                await member.add_roles(role, reason="Joined Co-working vc")
                await sendActivityMessage(
                    self.bot,
                    f"{member.name}#{member.discriminator} joined {after_channel.name}",
                )
                logEvent(
                    "coworking",
                    f"joined {after_channel.name}",
                    f"{member.name}#{member.discriminator}",
                )
            elif before_channel and before_channel.id in coworking_channel_ids:
                await member.remove_roles(role, reason="Left Co-working vc")
                await sendActivityMessage(
                    self.bot,
                    f"{member.name}#{member.discriminator} left {before_channel.name}",
                )
                logEvent(
                    "coworking",
                    f"left {before_channel.name}",
                    f"{member.name}#{member.discriminator}",
                )

        except Exception as e:
            await sendFalloutMessage(self.bot, e)


async def setup(bot):
    await bot.add_cog(coworking(bot))
