try:
    from txgeonames import client, interface
    from maxims.contrib import txgeonames
    txgeonames  # shut up pyflakes
except ImportError:  # pragma: no cover
    txgeonames = None

import mock
from axiom import store
from twisted.trial import unittest


def _makePersistedClient(store):
    return txgeonames.PersistedGeonamesClient(store=store, username=u"x")



class ActivationTests(unittest.TestCase):
    """
    Tests that the persisted client creates a real client when activated.
    """
    skip = txgeonames is None

    def test_activate(self):
        with mock.patch("txgeonames.client.GeonamesClient") as m:
            c = _makePersistedClient(store.Store())
            m.assert_called_once_with(u"x")
            self.assertIdentical(c.indirected, m.return_value)



class PowerupTests(unittest.TestCase):
    """
    Tests that the persisted Geonames client works as a powerup.
    """
    skip = txgeonames is None

    def setUp(self):
        self.store = store.Store()
        self.persisted = _makePersistedClient(self.store)
        self.store.powerUp(self.persisted)


    def test_powerup(self):
        """
        Tests that the store can be adapted.
        """
        inMemory = interface.IGeonamesClient(self.store)
        self.assertTrue(isinstance(inMemory, client.GeonamesClient))
        self.assertIdentical(self.persisted.indirected, inMemory)
