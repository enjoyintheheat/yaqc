from abc import ABC, abstractmethod
from enum import Enum, unique

'''
TODO:
- Reconnection func
'''


class ISocketZMQ(ABC):
    def __init__(self, ip_addr='*', port='5555'):
        self.ip_addr = ip_addr
        self.port = port

    @abstractmethod
    def acquire(self):
        '''Acquire ZeroMQ socket'''

    @abstractmethod
    def release(self):
        '''Release ZeroMQ socket'''

    @abstractmethod
    def detail(self):
        '''Detail information about subclass socket'''

    @property
    def address(self):
        return f'{self.ip_addr}:{self.port}'


@unique
class ConnectionState(Enum):
    CREATED = 1
    CONNECTED = 2
    CLOSED = 3