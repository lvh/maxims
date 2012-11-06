Creation time logging
=====================

You can log the creation time of any item by calling ``logCreation`` on it. The creation time can later be queried by calling ``creationTime``.

Automatic logging for an item class
-----------------------------------

You can automatically log the creation time of all instances of an item class with the ``@creationLogged`` decorator. This decorator causes the item instance to have its creation time logged when the ``stored`` callback fires: that is, when an item is added to the store for the first time.

.. testsetup::

    from axiom import attributes, item, store
    from maxims import creation

.. doctest::

    >>> @creation.creationLogged
    ... class Logged(item.Item):
    ...     dummyAttribute = attributes.boolean()
    >>> logged = Logged(store=store.Store())
    >>> creation.creationTime(logged)

Doing this when the item is first added to the store is generally what you want, since:

- Items are generally put into a store at creation or very soon after creation
- It's done using a documented callback instead of a hack into ``Item``'s internals
- Creation time logging requires item references to work. While references work without a store, there's no obvious way to transport all of the items into a store afterwards.

Note that manual creation time logging works fine with or without stores.
