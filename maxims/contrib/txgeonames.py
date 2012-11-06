"""
A persisted txgeonames client.
"""
from __future__ import absolute_import

from axiom import attributes, item
from txgeonames import client, interface as itxgeonames
from zope import interface


class PersistedGeonamesClient(item.Item):
    """
    A persisted Geonames client.

    This can be installed as a powerup like so::

        client = PersistedGeonamesClient(store=s, username=u"demo")
        empowered.powerup(client)

    Please note that changes to the username will only take effect after the
    next time this object is loaded from a store.
    """
    interface.implements(itxgeonames.IGeonamesClient)
    _interfaceNames = set(itxgeonames.IGeonamesClient.names())

    powerupIntefaces = [itxgeonames.IGeonamesClient]

    _client = attributes.inmemory()
    username = attributes.text(allowNone=False)

    def activate(self):
        """
        Creates an in-memory Geonames client.
        """
        self._client = client.GeonamesClient(self.username)


    def __getattr__(self, attr):
        """
        Gets interface methods from the in-memory client.
        """
        if attr in self.__class__._interfaceNames:
            return getattr(self._client, attr)

        raise AttributeError("no interface attribute {}".format(attr))
