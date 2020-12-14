from abc import ABC, abstractmethod

class IQueueController(ABC):
    @abstractmethod
    async def put(self, elem):
        '''Put method for async queue object'''

    @abstractmethod
    async def get(self):
        '''Get method for async queue object'''


'''
TODO:
- Queue class wrapper, that controls usage of async queue and:
    -) Notify about fullness
    -) Callback on_delete for queue instance
'''


class QueueController(IController):
    def __init__(self, queue):
        self._queue = queue

    async def put(self, elem):
        await self._queue.put(elem)

    async def get(self):
        return await self._queue.get()