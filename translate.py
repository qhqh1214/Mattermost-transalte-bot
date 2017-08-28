import re

from mattermost_bot.bot import listen_to

# translate KR - EN
@listen_to('`Kr` (.*)')
def KR_translate(message, translate):
    message.send('`En` : %s' % translate)

# translate EN - KR
@listen_to('`En` (.*)')
def EN_translate(message, translate):
    message.send('`Kr` : %s' % translate)
