import asyncio
import aiohttp
import discord

def init(loop=None):
    if not loop:
        loop = asyncio.get_event_loop()
    return Server(loop)

class Server(object):
    def __init__(self, loop):
        pass
    def run(self):
        self._loop.run_forever()
