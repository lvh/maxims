from axiom import attributes, item

from twisted.internet import endpoints, reactor


class _Endpoint(object):
    """
    An endpoint, stored by its description.
    """
    reactor = reactor

    def instantiate(self):
        return self.factory(self.reactor, self.description)



class ClientEndpoint(_Endpoint, item.Item):
    """
    A persisted client endpoint.
    """
    description = attributes.bytes(allowNone=False)
    factory = staticmethod(endpoints.clientFromString)



class ServerEndpoint(item.Item, _Endpoint):
    """
    A persisted server endpoint.
    """
    description = attributes.bytes(allowNone=False)
    factory = staticmethod(endpoints.serverFromString)