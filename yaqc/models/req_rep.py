import zmq
import zmq.asyncio
from .interfaces import ISocketZMQ


ctx = zmq.asyncio.Context()


class RequestZMQ(ISocketZMQ):
    def __init__(self, ip_addr='127.0.0.1', port='5555'):
        super().__init__(ip_addr, port)
        self._socket = RequestZMQ.acquire()

    async def __aenter__(self):
        self._socket.connect(f'tcp://{self.address}')
        return self._socket

    async def __aexit__(self, *exc):
        self._socket.close()

    def __repr__(self):
        return f'<REQ:{self.address}>'

    def acquire():
        return ctx.socket(zmq.REQ)

    def release(self):
        if self._socket:
            self._socket.close()


class ResponseZMQ(SocketZMQ):
    def __init__(self, ip_addr='127.0.0.1', port='5555'):
        super().__init__(ip_addr, port)
        self._socket = ResponseZMQ.acquire()

    async def __aenter__(self):
        self._socket.bind(f'tcp://{self.address}')
        return self._socket

    async def __aexit__(self, *exc):
        self._socket.close()

    def __repr__(self):
        return f'<REP:{self.binded_addr}>'

    def acquire():
        return ctx.socket(zmq.REP)

    def release(self):
        if self._socket:
            self._socket.close()