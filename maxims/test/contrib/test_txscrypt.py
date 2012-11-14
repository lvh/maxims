"""
Tests for txscrypt-stored credentials.
"""
try:
    from maxims.contrib import txscrypt
    txscrypt  # shut up pyflakes
except ImportError:  # pragma: no cover
    txscrypt = None

import mock

from axiom import store
from twisted.cred import credentials
from twisted.internet import defer
from twisted.trial import unittest


class UsernameScryptedPasswordTests(unittest.TestCase):
    """
    Tests for the scrypt-based ``IUsernameHashedPassword`` implementation.
    """
    skip = txscrypt is None

    def setUp(self):
        p = mock.patch("txscrypt.wrapper.verifyPassword")
        self.mockVerifyPassword = p.start()
        self.mockVerifyPassword.return_value = defer.succeed(True)
        self.addCleanup(p.stop)

        p = mock.patch("txscrypt.wrapper.computeKey")
        self.mockComputeKey = p.start()
        self.mockComputeKey.return_value = defer.succeed("key")
        self.addCleanup(p.stop)


    def test_checkPassword(self):
        """
        Tests that ``checkPassword`` defers to txscrypt's ``verifyPassword``.
        """
        c = txscrypt.UsernameScryptedPassword(username="u", _encrypted="key")
        c.checkPassword("provided")
        self.mockVerifyPassword.assert_called_once_with("key", "provided")


    def test_storePassword(self):
        """
        Tests that ``storePassword`` defers to txscrypt's ``computeKey``, and
        then stores its return value.
        """
        d = txscrypt.UsernameScryptedPassword.storePassword("u", "p", kw=1)
        self.mockComputeKey.assert_called_once_with("p", kw=1)
        return d.addCallback(self._checkUsernameHashedPassword)


    def test_addPowerupFor(self):
        """
        Tests that the class can correctly install a powerup on a store.
        """
        s = store.Store()
        d = txscrypt.UsernameScryptedPassword.addPowerupFor(s, "u", "p", kw=1)
        self.mockComputeKey.assert_called_once_with("p", kw=1)

        @d.addCallback
        def checkPowerup(usernameHashedPassword):
            powerup = credentials.IUsernameHashedPassword(s)
            self.assertIdentical(powerup, usernameHashedPassword)
            self._checkUsernameHashedPassword(usernameHashedPassword)

        return d


    def _checkUsernameHashedPassword(self, usernameHashedPassword):
        """
        Tests that the ``usernameHashedPassword`` has username and _encrypted
        attributes set to the appropriate values.
        """
        self.assertEqual(usernameHashedPassword.username, "u")
        self.assertEqual(usernameHashedPassword._encrypted, "key")
