try:
    from txeasymail import interface, mailer
    from maxims.contrib import txeasymail
    txeasymail  # shut up pyflakes
except ImportError:  # pragma: no cover
    txeasymail = None

import mock

from axiom import store
from maxims import credentials, endpoints
from twisted.trial import unittest


def _makePersistedMailer(store):
    mailerEndpoint = endpoints.ServerEndpoint(store=store,
        description="tcp:0")
    mailerCredentials = credentials.UsernamePassword(store=store,
        username="abc", password="xyz")
    persistedMailer = txeasymail.PersistedMailer(store=store,
        endpoint=mailerEndpoint, credentials=mailerCredentials)
    return persistedMailer



class ActivationTests(unittest.TestCase):
    """
    Tests that the persisted mailer creates a real mailer when activated.
    """
    skip = txeasymail is None

    def setUp(self):
        self.store = store.Store()


    def test_activate(self):
        with mock.patch("txeasymail.mailer.Mailer") as m:
            p = _makePersistedMailer(self.store)
            m.assert_called_once_with(*self._expectedCallArgs(p))
            self.assertIdentical(p.indirected, m.return_value)


    def _expectedCallArgs(self, persisted):
        return persisted.endpoint.instantiate(), persisted.credentials



class PowerupTests(unittest.TestCase):
    """
    Tests that the persisted mailer works as a powerup.
    """
    skip = txeasymail is None

    def setUp(self):
        self.store = store.Store()
        self.persisted = _makePersistedMailer(self.store)
        self.store.powerUp(self.persisted)


    def test_powerup(self):
        inMemory = interface.IMailer(self.store)
        self.assertTrue(isinstance(inMemory, mailer.Mailer))
        self.assertIdentical(self.persisted.indirected, inMemory)
