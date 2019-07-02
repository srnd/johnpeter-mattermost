# John Peter
Mattermost helper chatbot using [mmpy_bot](https://github.com/attzonko/mmpy_bot)

Note: To run, the system needs the following environment variables to be set: 
```
MATTERMOST_BOT_URL=https://<mattermost server url>/api/v4
MATTERMOST_BOT_LOGIN=<bot account username>
MATTERMOST_BOT_PASSWORD=<bot account password>
MATTERMOST_BOT_TEAM=<team name>
MATTERMOST_BOT_TOKEN=<bot token>
```

The team name, if unknown, is visible in the URL. For example, with SRND's chat (chat.srnd.org), the "Town Square" channel in the "Community" team has the url `https://chat.srnd.org/srnd/channels/town-square`.
If you wanted to have the bot work in the "Community" team, then you would use `srnd` as the `MATTERMOST_BOT_TEAM` variable.

##Adding Plugins
TODO