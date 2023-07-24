from os import environ
from json import loads
from dotenv import load_dotenv

load_dotenv()

# general
discord_token = environ["DISCORD_TOKEN"]
activity_channel_id = int(environ["ACTIVITY_CHANNEL_ID"])
fallout_channel_id = int(environ["FALLOUT_CHANNEL_ID"])

# coworking
coworking_role_id = int(environ["COWORKER_ROLE_ID"])
coworking_channel_ids: list[int] = loads(environ["COWORKING_CHANNELS_IDS"])

# cams_only
cam_only_channel_ids = loads(environ["CAM_ONLY_CHANNELS_IDS"])
cams_only_warn_period = int(environ["CAMS_ONLY_WARN_PERIOD"])
cams_only_kick_period = int(environ["CAMS_ONLY_KICK_PERIOD"])
cams_only_move_vc_id = int(environ["CAMS_ONLY_MOVE_VC_ID"])

# cams only next level
cams_only_warn_period_nextlevel = int(environ["CAMS_ONLY_WARN_PERIOD_NEXTLEVEL"])
cams_only_kick_period_nextlevel = int(environ["CAMS_ONLY_KICK_PERIOD_NEXTLEVEL"])
role_nextlevel = environ["NEXTLEVEL"]
