from abc import ABC, abstractmethod
from asyncio import Queue

class IController(ABC):
    pass


class Controller:
    def __init__(self, max_size=100):
        self._queue = Queue(maxsize=max_size)

    async def put(self, elem):
        await self._queue.put(elem)

    async def get(self):
        return await self._queue.get()