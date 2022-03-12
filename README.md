# watcher

Discord bot for self.dev community

## Main Idea

The main idea is to have a discord bot that solves all our co-working needs and provides some interesting data about the same, (long suggested very cool).
So for now, having a pingable co-worker role and some interesting data would be nice.

Tech Details

- Python for scripting
- MongoDB for storing the data

## Contributing

- Fork the repo and activate your virtual env
- install the dependencies
- make .env file and insert required variables

```
pip install -r requirements.txt
touch .env
```

### Env Variables

```
MONGODB_URI=mongodb://localhost:27017/watcher
DISCORD_TOKEN=discord token
COWORKER_ROLE_ID=coworker role id
COWORKING_CHANNELS_IDS=[coworking channel ids<int>]
FALLOUT_CHANNEL_ID=fallout channel id to send production breaking errors
```

Contributors

- [Arth](https://github.com/probablyArth)
