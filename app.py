import json
from configparser import ConfigParser

import requests
from flask import Flask, request

config = ConfigParser()
config.read('config.ini')

states = {}
app = Flask(__name__)


@app.route('/chat', methods=['POST'])
def chat():
    global states
    message = json.loads(request.data)
    state_id = message['user_id'] + message['channel_id']  # So each user/channel combo has unique state
    if state_id not in states:
        states[state_id] = None
    # remove first instance of trigger word (So "john hi" is sent to cleverbot as "hi")
    msg_in = message['text'].replace(message['trigger_word'], '', 1)  # https://stackoverflow.com/a/10648554/4991969
    r = requests.get(
        url='http://www.cleverbot.com/getreply?key={}&input={}&cs={}'.format(config['cleverbot']['API_KEY'], msg_in,
                                                                             states[state_id]), verify=False)
    msg_out = json.loads(r.text)['output']
    states[state_id] = json.loads(r.text)['cs']
    return '{"text":"{}"}'.format(msg_out)
