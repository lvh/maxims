import sys
import mock
sys.modules["txeasymail"] = txeasymailMocked = mock.Mock()

from twisted.trial import unittest

from maxims.contrib import txeasymail


class TxeasymailTests(unittest.TestCase):
    def test_instantiate(self):
        ep, c = mock.Mock(), mock.Mock()
        ep.__legacy__ = c.__legacy__ = False

        mc = txeasymail.MailerConfiguration(endpoint=ep, credentials=c)
        mc.instantiate()

        (args, kwargs), = txeasymailMocked.mailer.Mailer.call_args_list
        self.assertEqual(kwargs, {})
        instantiatedEndpoint, instantiatedCredentials = args
        self.assertEqual(instantiatedEndpoint, ep.instantiate.return_value)
        self.assertEqual(instantiatedCredentials, c.instantiate.return_value)
