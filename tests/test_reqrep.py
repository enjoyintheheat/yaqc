import asyncio
import sys
import pytest
from yaqc.models.req_rep import RequestZMQ, ResponseZMQ
from yaqc.models.interfaces import ConnectionState

# For testing purposes on Win Platform
if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


@pytest.mark.asyncio
async def test_requestzmq_instance():
    req = RequestZMQ()
    req_detail = req.detail()
    assert req.__class__.__name__ == req_detail['name']
    assert '127.0.0.1' == req_detail['ip']
    assert '5555' == req_detail['port']
    assert ConnectionState.CREATED == req_detail['state']

@pytest.mark.asyncio
async def test_requestzmq_instance():
    res = ResponseZMQ()
    res_detail = res.detail()
    assert res.__class__.__name__ == res_detail['name']
    assert '127.0.0.1' == res_detail['ip']
    assert '5555' == res_detail['port']
    assert ConnectionState.CREATED == res_detail['state']
