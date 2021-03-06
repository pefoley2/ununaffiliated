from asyncirc import irc
import blinker
import config

connected_signals = []
def connect_signal(signal_name, func):
    connected_signals.append((signal_name, func))
    blinker.signal(signal_name).connect(func)

def clear_signals():
    while connected_signals:
        k = connected_signals.pop()
        blinker.signal(k[0]).disconnect(k[1])

bot = irc.connect("chat.freenode.net")
bot.register(config.nickname, config.ident, config.realname)
