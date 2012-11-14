try:
    from txeasymail import interface, mailer
    from maxims.contrib import txeasymail
    txeasymail  # shut up pyflakes
except ImportError:  # pragma: no cover
    txeasymail = None

from maxims import credentials, endpoints
from maxims.test import indirection
from twisted.trial import unittest


def _makePersistedMailer(store):
    mailerEndpoint = endpoints.ServerEndpoint(store=store,
        description="tcp:0")
    mailerCredentials = credentials.UsernamePassword(store=store,
        username="abc", password="xyz")
    persistedMailer = txeasymail.PersistedMailer(store=store,
        endpoint=mailerEndpoint, credentials=mailerCredentials)
    return persistedMailer



class ActivationTests(indirection.ActivationTests, unittest.TestCase):
    """
    Tests that the persisted mailer creates a real mailer when activated.
    """
    skip = txeasymail is None

    makePersistedObject = staticmethod(_makePersistedMailer)
    implementationLocation = "txeasymail.mailer.Mailer"

    def _expectedCallArgs(self, persisted):
        return persisted.endpoint.instantiate(), persisted.credentials



class PowerupTests(indirection.PowerupTests, unittest.TestCase):
    """
    Tests that the persisted mailer works as a powerup.
    """
    skip = txeasymail is None

    makePersistedObject = staticmethod(_makePersistedMailer)
    interface, implementation = interface.IMailer, mailer.Mailer
