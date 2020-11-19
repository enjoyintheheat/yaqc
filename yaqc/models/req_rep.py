import zmq
import zmq.asyncio
from .socket import SocketZMQ


ctx = zmq.asyncio.Context()


class RequestZMQ(SocketZMQ):
    def __init__(self, ip_addr='127.0.0.1', port='5555'):
        super(RequestZMQ, self).__init__(ip_addr, port)
        self._socket = RequestZMQ.acquire()

    async def __aenter__(self):
        self._socket.connect(f'tcp://{self.address}')
        return self._socket

    async def __aexit__(self, *exc):
        self._socket.close()

    def __repr__(self):
        return f'<REQ:{self.address}>'

    @staticmethod
    def acquire():
        return ctx.socket(zmq.REQ)

    def release(self):
        if self._socket:
            self._socket.close()


class ResponseZMQ(SocketZMQ):
    def __init__(self, ip_addr='*', port='5556'):
        super(ResponseZMQ, self).__init__(ip_addr, port)
        self._socket = ResponseZMQ.acquire()

    def __aenter__(self):
        self._socket.bind(f'tcp://{self.address}')
        return self._socket

    def __aexit__(self, *exc):
        self._socket.close()

    def __repr__(self):
        return f'<REP:{self.binded_addr}>'

    @staticmethod
    def acquire():
        return ctx.socket(zmq.REP)

    def release(self):
        if self._socket:
            self._socket.close()