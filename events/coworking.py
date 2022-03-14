from os import environ
from discord.ext import commands
from json import loads

role_id = int(environ['COWORKER_ROLE_ID'])
channel_ids = loads(environ['COWORKING_CHANNELS_IDS'])
fallout_channel_id = int(environ['FALLOUT_CHANNEL_ID'])

class coworking(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    print('Co-working events loaded!')
    
  @commands.Cog.listener()
  async def on_voice_state_update(self, member, before, after):
    
    try:
      guild = self.bot.get_guild(member.guild.id)
      role = guild.get_role(role_id)
      before_channel = before.channel
      after_channel = after.channel

      if after_channel and after_channel.id in channel_ids:
        await member.add_roles(role, reason='Joined Co-working vc')

      elif before_channel and before_channel.id in channel_ids:
        await member.remove_roles(role, reason='Left Co-working vc')
    except AttributeError:
      fallout_channel = member.guild.get_channel(fallout_channel_id)
      await fallout_channel.send(f"Coworker role with id `{role_id}` doesn't exist! Please update env variables in production :pray:")

def setup(bot):
  bot.add_cog(coworking(bot))
