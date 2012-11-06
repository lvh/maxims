try:
    from txgeonames import client, interface
    from maxims.contrib import txgeonames
    txgeonames  # shut up pyflakes
except ImportError:  # pragma: no cover
    txgeonames = None

from maxims.test import indirection
from twisted.trial import unittest


def _makePersistedClient(store):
    return txgeonames.PersistedGeonamesClient(store=store, username=u"x")



class ActivationTests(indirection.ActivationTests, unittest.TestCase):
    """
    Tests that the persisted client creates a real client when activated.
    """
    skip = txgeonames is None

    makePersistedObject = staticmethod(_makePersistedClient)
    implementationLocation = "txgeonames.client.GeonamesClient"

    def _expectedCallArgs(self, persisted):
        return u"x",



class PowerupTests(unittest.TestCase):
    """
    Tests that the persisted Geonames client works as a powerup.
    """
    skip = txgeonames is None

    makePersistedObject = staticmethod(_makePersistedClient)
    interface = interface.IGeonamesClient
    implementation = client.GeonamesClient
