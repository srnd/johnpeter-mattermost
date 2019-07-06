import re
from mmpy_bot.bot import listen_to


@listen_to('^(\w) job tj$', re.IGNORECASE)
def good_job_tj(message,job):
    message.send('yes tj did a {} job'.format(job))