"""
Tests for txscrypt-stored credentials.
"""
try:
    from maxims.contrib import txscrypt
    txscrypt  # shut up pyflakes
except ImportError:  # pragma: no cover
    txscrypt = None

from axiom import store
from twisted.cred import credentials
from twisted.internet import defer
from twisted.trial import unittest


class UsernameScryptedPasswordTests(unittest.TestCase):
    """
    Tests for the scrypt-based ``IUsernameHashedPassword`` implementation.
    """
    skip = txscrypt is None

    @defer.inlineCallbacks
    def setUp(self):
        storePassword = txscrypt.UsernameScryptedPassword.storePassword
        self.stored = yield storePassword("u", "p", maxTime=0.0001)


    @defer.inlineCallbacks
    def _assertStoredPasswordWorks(self, stored):
        yield stored.checkPassword("p").addCallback(self.assertEqual, True)
        yield stored.checkPassword("x").addCallback(self.assertEqual, False)

 
    def test_checkPassword(self):
        """
        Tests that when the right password is provided, ``checkPassword``
        returns ``True``, and when the wrong password is provided, it returns
        ``False``.
        """
        return self._assertStoredPasswordWorks(self.stored)


    @defer.inlineCallbacks
    def test_addPowerupFor(self):
        """
        Tests that the class can correctly install a powerup on a store.
        """
        s = store.Store()
        addPowerupFor = txscrypt.UsernameScryptedPassword.addPowerupFor
        returned = yield addPowerupFor(s, "u", "p", maxTime=0.001)

        stored = credentials.IUsernameHashedPassword(s)
        self.assertIdentical(returned, stored)
        yield self._assertStoredPasswordWorks(stored)
