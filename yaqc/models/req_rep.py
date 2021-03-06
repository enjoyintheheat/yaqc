import zmq
from zmq.asyncio import Context
from .interfaces import ISocketZMQ, ConnectionState


class RequestZMQ(ISocketZMQ):
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

    def __repr__(self):
        return f'<REQ:{self.address}>'

    def acquire(self):
        return self._ctx.socket(zmq.REQ)

    def release(self):
        if self._socket:
            self._socket.close()

    def detail(self):
        return {'name': self.__class__.__name__, 'ip': self.ip_addr,
                'port': self.port, 'state': self._state}


class ResponseZMQ(ISocketZMQ):
    def __init__(self, ip_addr='127.0.0.1', port='5555'):
        super().__init__(ip_addr, port)
        self._ctx = Context.instance()
        self._socket = self.acquire()
        self._state = ConnectionState.CREATED

    async def __aenter__(self):
        self._socket.bind(f'tcp://{self.address}')
        self._state = ConnectionState.CONNECTED
        return self._socket

    async def __aexit__(self, *exc):
        self._socket.close()
        self._state = ConnectionState.CLOSED

    def __repr__(self):
        return f'<REP:{self.binded_addr}>'

    def acquire(self):
        return self._ctx.socket(zmq.REP)

    def release(self):
        if self._socket:
            self._socket.close()

    def detail(self):
        return {'name': self.__class__.__name__, 'ip': self.ip_addr,
                'port': self.port, 'state': self._state}