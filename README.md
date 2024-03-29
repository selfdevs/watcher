# watcher

Discord bot for self.dev community

## Current features

- add/remove co-working role when member joins/leaves a coworking VC.
- warn and kick the user from select voice channels if they don't turn on their cams.

## Running the project locally

### Project setup

```
# install dependencies
pip install -r requirements.txt

# make .env file from .env.example
cp .env.example .env

# run
python3 bot.py
```

Update the variables in `.env` manually

### Running as docker container

```sh
docker run --env (ENV1="something"...Add env variables here manually) -v "absolute/path/to/where/you/want/to/store/logs:/app/data" probablyarth/selfdevs-watcher:1.0
```

or load env variables from a file

```sh
docker run --env-file "path to .env file" -v "absolute/path/to/where/you/want/to/store/logs:/app/data" probablyarth/selfdevs-watcher:1.0
```

### Discord developer portal

#### Intents

![SERVER MEMBERS INTENT, MESSAGE CONTENT INTENT](./.github/assets/intents.png)

#### Permissions

![Manage Roles, Read Message/View Channels, Send Messages, Send Messages In Threads, Move Members](./.github/assets/permissions.png)

## Project structure

```
.
|- events
|    |- coworking.py # events related to coworking channels
|    |- cams_only.py # events related to cams_only channels
|- utils.py          # all the utility functions to keep it DRY.
|- env.py            # single source of env variables
|- bot.py            # main entrypoint

```

For contributing refer [CONTRIBUTING](https://github.com/selfdevs/watcher/blob/v1/CONTRIBUTING.md)

Contributors

- [Arth](https://github.com/probablyArth)
