# John Peter
Mattermost helper chatbot using [mmpy_bot](https://github.com/attzonko/mmpy_bot)

Note: To run, the system needs the following environment variables to be set: 
```
MATTERMOST_BOT_URL=https://<mattermost server url>/api/v4
MATTERMOST_BOT_LOGIN=<bot account username>
MATTERMOST_BOT_PASSWORD=<bot account password>
MATTERMOST_BOT_TEAM=<team name>
MATTERMOST_BOT_TOKEN=<bot token>
CLEVERBOT_API_KEY=<cleverbot api key>
```

The team name, if unknown, is visible in the URL. For example, with SRND's chat (chat.srnd.org), the "Town Square" channel in the "Community" team has the url `https://chat.srnd.org/srnd/channels/town-square`.
If you wanted to have the bot work in the "Community" team, then you would use `srnd` as the `MATTERMOST_BOT_TEAM` variable.

##Adding Plugins
To add functionality, create a new file in the `./mmpy_bot/plugins/` folder. For example, say we wanted to make John say "Hello there!" whenever a user says "hi".
First, let's create a file named `hello.py` and add the following lines of code:

```python
import re
from mmpy_bot.bot import listen_to
```
This imports the regex module and the `listen_to` decorator. 
Then we can expand upon it by adding the following: 
```python
@listen_to('hi',re.IGNORECASE)
def hi(message):
    message.send('Hello there!')
```
Combined, this is all you need for basic bot functionality. Pull requests are welcome with additional features.
