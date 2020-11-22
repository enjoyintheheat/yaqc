from asyncio import Queue

class Controller:
    def __init__(self, max_size=100):
        self.queue = Queue(maxsize=max_size)