import asyncio
import zmq
import zmq.asyncio
from contextlib import suppress
from weakref import WeakSet
from models.req_rep import RequestZMQ, ResponseZMQ


async def sender():
    with suppress(asyncio.CancelledError):
        async with RequestZMQ() as req_socket:
            while True:
                await req_socket.send_json({'msg': 'hello'})
                data = await req_socket.recv_json()
                print(data)
                await asyncio.sleep(1)


async def receiver():
    with suppress(asyncio.CancelledError):
        async with ResponseZMQ() as rep_socket:
            while True:
                data = await rep_socket.recv_json()
                print(data)
                await rep_socket.send_json({'code': 200})
                await asyncio.sleep(1)


async def main():
    await asyncio.gather(receiver(), sender())


if __name__ == '__main__':
    try:
        print('Starting listen TCP SUB socket on localhost:5555')
        one_req = RequestZMQ()
        one_res = ResponseZMQ()
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Finishing...')
