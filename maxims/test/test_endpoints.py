from twisted.internet import endpoints
from twisted.trial import unittest

from maxims import endpoints as me


class ClientEndpointTests(unittest.TestCase):
    def test_instantiate(self):
        ep = me.ClientEndpoint(description="tcp:x:1").instantiate()
        self.assertTrue(isinstance(ep, endpoints.TCP4ClientEndpoint))
        self.assertEqual(ep._host, "x")
        self.assertEqual(ep._port, 1)



class ServerEndpointTests(unittest.TestCase):
    def test_instantiate(self):
        ep = me.ServerEndpoint(description="tcp:1").instantiate()
        self.assertTrue(isinstance(ep, endpoints.TCP4ServerEndpoint))
        self.assertEqual(ep._port, 1)
