import zmq
from zmq.asyncio import Context
from .interfaces import ISocketZMQ, ConnectionState


class PublishZMQ(ISocketZMQ):
    def __init__(self, ip_addr='127.0.0.1', port='5555'):
        super().__init__(ip_addr, port)
        self._ctx = Context.instance()
        self._socket = self.acquire()
        self._state = ConnectionState.CREATED

    async def __aenter__(self):
        self._socket.connect(f'tcp://{self.address}')
        self._state = ConnectionState.CONNECTED
        return self._socket

    async def __aexit__(self, *exc):
        self._socket.close()
        self._state = ConnectionState.CLOSED

    def acquire(self):
        return self._ctx.socket(zmq.PUB)

    def release(self):
        if self._socket:
            self._socket.close()


class SubscribeZMQ(ISocketZMQ):
    def __init__(self, ip_addr='127.0.0.1', port='5555'):
        super().__init__(ip_addr, port)
        self._socket = self.acquire()

    async def __aenter__(self):
        self._socket.bind(f'tcp://{self.address}')
        self._state = ConnectionState.CONNECTED
        return self._socket

    async def __aexit__(self, *exc):
        self._socket.close()
        self._state = ConnectionState.CLOSED

    def acquire(self):
        return self._ctx.socket(zmq.SUB)

    def release(self):
        if self._socket:
            self._socket.close()