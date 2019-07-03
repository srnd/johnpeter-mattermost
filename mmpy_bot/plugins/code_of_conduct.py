import re
from mmpy_bot.bot import listen_to


@listen_to('^code of conduct$',re.IGNORECASE)
def code_of_conduct(message):
    message.send('https://srnd.org/conduct')