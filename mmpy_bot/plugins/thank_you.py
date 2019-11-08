import re, random
from mmpy_bot.bot import listen_to


@listen_to('^thanks?,? (you,? )?john!?$', re.IGNORECASE)  # "Thanks john", "Thanks, john!", "Thank you john" and more
def thank_you(message,input): # Needs second argument for whatever reason too lazy to figure it out
    you_apostrophe_re_welcome = ['I am in no need of your human thanks!',
                                 'No, thank **you**! :blush:',
                                 'Much appreciated, fellow human!',
                                 'Happy to help',
                                 'message.send(random.choice(you_apostrophe_re_welcome))',
                                 'THIS ACTION COST {} JOHN CREDITS. JOHN CREDITS REMAINING: {}'.format(random.randint(1, 10),random.randint(70, 200)),
                                 'You\'re welcome!']
    message.send(random.choice(you_apostrophe_re_welcome))
