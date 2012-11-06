try:
    from txgeonames import client
    from maxims.contrib import txgeonames
    client, txgeonames  # shut up pyflakes
except ImportError:
    client = txgeonames = None

import mock
from axiom import store

from twisted.trial import unittest


def _makeClient():
    c = txgeonames.PersistedGeonamesClient(
        store=store.Store(),
        username=u"x"
    )
    return c


class ActivationTests(unittest.TestCase):
    """
    Tests that the persisted client creates a real client on activation.
    """
    skip = txgeonames is None

    def test_activate(self):
        with mock.patch("txgeonames.client.GeonamesClient") as m:
            c = _makeClient()
            m.assert_called_once_with(u"x")
            self.assertIdentical(c._client, m.return_value)



class InterfaceProxyingTests(unittest.TestCase):
    """
    Tests that attributes defined on the interface get proxied correctly,
    and *only* those attributes do.
    """
    skip = txgeonames is None

    def setUp(self):
        self.client = _makeClient()


    def test_interfaceMethod(self):
        """
        Tests that interface attribute access on the persisted client gets
        proxied to an actual client.
        """
        actual = self.client.postalCodeLookup.im_func
        expected = client.GeonamesClient.postalCodeLookup.im_func
        self.assertIdentical(actual, expected)


    def test_noInterfaceMethod(self):
        """
        Tests that accessing attributes not defined on the interface raises
        ``AttributeError``.
        """
        self.assertRaises(AttributeError, getattr, self.client, "BOGUS")
