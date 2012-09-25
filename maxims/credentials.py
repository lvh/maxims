from axiom import attributes, item
from twisted.cred import credentials


class UsernamePassword(item.Item):
    """
    A stored username and password.
    """
    username = attributes.bytes(allowNone=False)
    password = attributes.bytes(allowNone=False)

    def instantiate(self):
        return credentials.UsernamePassword(self.username, self.password)
