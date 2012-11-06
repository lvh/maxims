"""
Tests for persisted endpoints.
"""
from twisted.internet import endpoints
from twisted.trial import unittest

from maxims import endpoints as me


class _EndpointTests(object):
    """
    Base endpoint tests.
    """
    def setUp(self):
        self.endpoint = self.endpointClass(description=self.description)


    def test_cached(self):
        """
        Tests that calling ``instantiate`` several times gets the same
        result.
        """
        one, two = self.endpoint.instantiate(), self.endpoint.instantiate()
        self.assertIdentical(one, two)



class ClientEndpointTests(_EndpointTests, unittest.TestCase):
    """
    Tests for client endpoints.
    """
    endpointClass, description = me.ClientEndpoint, "tcp:x:1"

    def test_instantiate(self):
        """
        Creates a client endpoint, checks it's of the expected type, and
        verifies its attributes.
        """
        ep = self.endpoint.instantiate()
        self.assertTrue(isinstance(ep, endpoints.TCP4ClientEndpoint))
        self.assertEqual(ep._host, "x")
        self.assertEqual(ep._port, 1)



class ServerEndpointTests(_EndpointTests, unittest.TestCase):
    """
    Tests for server endpoints.
    """
    endpointClass, description = me.ServerEndpoint, "tcp:1"

    def test_instantiate(self):
        """
        Creates a server endpoint, checks it's of the expected type, and
        verifies its attributes.
        """
        ep = me.ServerEndpoint(description="tcp:1").instantiate()
        self.assertTrue(isinstance(ep, endpoints.TCP4ServerEndpoint))
        self.assertEqual(ep._port, 1)
