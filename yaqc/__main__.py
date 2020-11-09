import asyncio
import zmq
import zmq.asyncio
from contextlib import suppress
import sys

if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

ctx = zmq.asyncio.Context()

async def main():
    sock = ctx.socket(zmq.SUB)
    sock.connect('tcp://localhost:5555')
    sock.setsockopt_string(zmq.SUBSCRIBE, '')
    with suppress(asyncio.CancelledError):
        while message := await sock.recv_json():
            print(message)
    sock.close()


if __name__ == '__main__':
    try:
        print('Starting listen TCP SUB socket on localhost:5555')
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Finishing...')
        ctx.term()