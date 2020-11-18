import zmq
import zmq.asyncio
from .socket import SocketZMQ


ctx = zmq.asyncio.Context()


class RequestZMQ(SocketZMQ):
    def __init__(self, ip_addr='127.0.0.1', port='5555'):
        super(RequestZMQ, self).__init__(ip_addr, port)
        self._socket = ctx.socket(zmq.REQ)
        print(self.address)
        self._socket.connect(f'tcp://{self.address}')

    def acquire(self):
        pass

    def release(self):
        pass

    def __repr__(self):
        return f'<REQ:{self.address}>'


class ResponseZMQ(SocketZMQ):
    def __init__(self, ip_addr='*', port='5556'):
        self._socket = ctx.socket(zmq.REP)
        self.binded_addr = f'{ip_addr}:{port}'
        self._socket.bind(f'tcp://{self.binded_addr}')

    def __repr__(self):
        return f'<REP:{self.binded_addr}>'