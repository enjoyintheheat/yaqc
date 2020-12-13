from abc import ABC, abstractmethod

class IController(ABC):
    @abstractmethod
    async def put(self, elem):
        '''Put method for async queue object'''

    @abstractmethod
    async def get(self):
        '''Get method for async queue object'''


class Controller(IController):
    def __init__(self, queue):
        self._queue = queue

    async def put(self, elem):
        await self._queue.put(elem)

    async def get(self):
        return await self._queue.get()