from __future__ import absolute_import

from axiom import attributes, item
from txeasymail import mailer


class MailerConfiguration(item.Item):
    endpoint = attributes.reference()
    credentials = attributes.reference()


    def instantiate(self):
        """
        Instantiates a mailer from this configuration.
        """
        args = [a.instantiate() for a in (self.endpoint, self.credentials)]
        return mailer.Mailer(*args)
