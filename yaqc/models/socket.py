import abc


class SocketZMQ(metaclass=abc.ABCMeta):
    def __init__(self, ip_addr='*', port='5555'):
        self.ip_addr = ip_addr
        self.port = port

    @abc.abstractmethod
    def acquire(self):
        '''Acquire ZeroMQ socket'''

    @abc.abstractmethod
    def release(self):
        '''Release ZeroMQ socket'''

    @property
    def address(self):
        return f'{self.ip_addr}:{self.port}'