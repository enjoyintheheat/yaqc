import asyncio
import zmq
import zmq.asyncio
from contextlib import suppress


ctx = zmq.asyncio.Context()


class PipelineController:
    def __init__(self, max_size=100):
        self.queue_in = asyncio.Queue(max_size)
        self.queue_out = asyncio.Queue(max_size)

    async def sub_main_topic(self, name='main', ip_addr='*', port='5555'):
        self.main_sock = ctx.socket(zmq.SUB)
        self.main_sock.connect(f'tcp://{ip_addr}:{port}')
        self.main_sock.setsockopt_string(zmq.SUBSCRIBE, name)


async def main():
    sock = ctx.socket(zmq.SUB)
    sock.connect('tcp://*:5555')
    sock.setsockopt_string(zmq.SUBSCRIBE, '1')
    with suppress(asyncio.CancelledError):
        while True:
            message = await sock.recv_json()
            print(message)
    sock.close()


if __name__ == '__main__':
    try:
        print('Starting listen TCP SUB socket on localhost:5555')
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Finishing...')
        ctx.term()
