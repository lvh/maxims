from twisted.cred import credentials
from twisted.trial import unittest

from maxims import credentials as mc


class UsernamePasswordTests(unittest.TestCase):
    def test_instantiate(self):
        username, password = "username", "password"
        up = mc.UsernamePassword(username=username, password=password)
        c = up.instantiate()

        self.assertEqual(c.username, username)
        self.assertEqual(c.password, password)

        self.assertTrue(credentials.IUsernamePassword.providedBy(c))
