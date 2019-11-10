import re
from mmpy_bot.bot import listen_to


@listen_to('^.* code day .*$', re.IGNORECASE)
def code_day(message):
    message.send('BRANDING')
