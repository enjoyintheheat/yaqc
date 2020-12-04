import pytest
from yaqc.models.req_rep import RequestZMQ
from yaqc.models.interfaces import ConnectionState


@pytest.mark.asyncio
async def test_requestzmq_instance():
    req = RequestZMQ()
    req_detail = req.detail()
    print(req_detail['name'])
    assert type(req).__name__ == req_detail['name']
    assert '127.0.0.1' == req_detail['ip']
    assert '5555' == req_detail['port']
    assert ConnectionState.CREATED == req_detail['state']