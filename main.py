# The actual script you run directly.
from bot_common import (
    bot, guild_config, member_stalker, stats_tracker, stored_suggestions,
    )

import cogs_dailycounts
import bot_events
import bot_modcommands
import bot_usercommands
import stupid_arquius_tricks
import cogs_rolemanager
import cogs_reactroletagger

def get_token() -> str:
    with open('token.dat', 'r') as tokenfile:
        raw = tokenfile.read().strip()
        return ''.join(chr(int(''.join(c), 16)) for c in zip(*[iter(raw)]*2))

if __name__ == '__main__':
    with guild_config, member_stalker, stats_tracker, stored_suggestions:
        bot.run(get_token())
