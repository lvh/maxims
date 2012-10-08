from axiom import attributes, item
from twisted.cred import credentials


class UsernamePassword(item.Item):
    """
    A stored username and password.

    Note that although this class is an ``IUsernamePassword`` implementation,
    you should still use the ``instantiate`` method to get independent
    ``IUsernamePassword`` providers.
    """
    username = attributes.bytes(allowNone=False)
    password = attributes.bytes(allowNone=False)

    def instantiate(self):
        return credentials.UsernamePassword(self.username, self.password)
