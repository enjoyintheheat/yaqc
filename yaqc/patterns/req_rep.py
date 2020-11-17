import zmq
import zmq.asyncio


ctx = zmq.asyncio.Context()


class RequestZMQ:
    def __init__(self, ip_addr='*', port='5555'):
        self._socket = ctx.socket(zmq.REQ)
        self.binded_addr = f'{ip_addr}:{port}'
        self._socket.connect(f'tcp://{self.binded_addr}')

    def __repr__(self):
        return f'<REQ:{self.binded_addr}>'


class ResponseZMQ:
    def __init__(self, ip_addr='*', port='5556'):
        self._socket = ctx.socket(zmq.REP)
        self.binded_addr = f'{ip_addr}:{port}'
        self._socket.bind(f'tcp://{self.binded_addr}')

    def __repr__(self):
        return f'<REP:{self.binded_addr}>'