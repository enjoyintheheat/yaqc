import unittest
from yaqc.models.req_rep import RequestZMQ


class ReqRepTest(unittest.TestCase):
    def setUp(self):
        self.req_zmq = RequestZMQ()

    def test_req_socket(self):
        print(self.req_zmq)