import os, re, requests, json
from mmpy_bot.bot import listen_to, respond_to
from mmpy_bot.utils import allow_only_direct_message, allowed_channels


states = {}  # initialize empty dict for states
API_KEY = os.getenv('CLEVERBOT_API_KEY')


@listen_to('^john (.+)$', re.IGNORECASE)  # only reply to messages in public channels that start with "john"
@respond_to('^(.+)$')  # also reply to all messages that ping john or are in DM
@allowed_channels('random','john-dev')  # also works in DM
def cleverbot(message,input):
    global states
    state_id = str(message.get_user_id()) + str(message.get_channel_name())  # each user/channel combo has unique state
    if state_id not in states:
        states[state_id] = None
    r = requests.get(url='http://www.cleverbot.com/getreply?key={}&input={}&cs={}'.format(API_KEY,input,states[state_id]), verify=False)
    msg_out = json.loads(r.text)['output']
    states[state_id] = json.loads(r.text)['cs']
    message.send(msg_out)