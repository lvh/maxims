"""
An easy way to persist objects that are otherwise not persistable,
as long as they can be instantiated by just passing them a store.
"""
from axiom import attributes, iaxiom, item
from twisted.python.reflect import fullyQualifiedName, namedAny
from zope import interface as zi


@zi.implementer(iaxiom.IPowerupIndirector)
class _StoredByName(item.Item):
    """
    A powerup indirector for something that is stored by name.
    """
    className = attributes.bytes(allowNone=False)

    def indirect(self, interface):
        """
        Instantiates the named class with this object's store, then adapts
        it to the given interface.
        """
        return interface(namedAny(self.className)(self.store))



def remember(empowered, powerupClass, interface):
    """
    Adds a powerup to ``empowered`` that will instantiate ``powerupClass``
    with the empowered's store when adapted to the given interface.

    :param empowered: The Empowered (Store or Item) to be powered up.
    :type empowered: ``axiom.item.Empowered``
    :param powerupClass: The class that will be powered up to.
    :type powerupClass: class
    :param interface: The interface of the powerup.
    :type interface: ``zope.interface.Interface``
    :returns: ``None``
    """
    className = fullyQualifiedName(powerupClass)
    powerup = _StoredByName(store=empowered.store, className=className)
    empowered.powerUp(powerup, interface)


def forget(empowered, powerupClass, interface):
    """
    Forgets powerups previously stored with ``remember``.

    :param empowered: The Empowered (Store or Item) to be powered down.
    :type empowered: ``axiom.item.Empowered``
    :param powerupClass: The class for which powerups will be forgotten.
    :type powerupClass: class
    :param interface: The interface the powerups were installed for.
    :type interface: ``zope.interface.Interface``
    :returns: ``None``
    :raises ValueError: Class wasn't previously remembered.
    """
    className = fullyQualifiedName(powerupClass)
    withThisName = _StoredByName.className == className
    items = empowered.store.query(_StoredByName, withThisName)

    if items.count() == 0:
        template = "No named powerups for {} (interface: {})".format
        raise ValueError(template(powerupClass, interface))

    for stored in items:
        empowered.powerDown(stored, interface)
        stored.deleteFromStore()
