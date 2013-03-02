Items
=====

Items are just commonly reusable Axiom items. They can represent
objects such as credentials, endpoints...

API
---

Things that can be persisted as Axiom items share a common API. The
item has an ``instantiate`` method taking no arguments, giving you a
new, independent instance of the object represented by that item.

.. testsetup::

    from maxims import endpoints

.. doctest::

    >>> storedEndpoint = endpoints.ServerEndpoint(description="tcp:0")
    >>> storedEndpoint.instantiate()
    <twisted.internet.endpoints.TCP4ServerEndpoint object at ...>

Alternatively, many items will allow you to use them directly as if
they implemented the interface of the object you'd usually have; for
example, that same ``ServerEndpoint`` implements the ``listen``
method:

.. testsetup::

    from twisted.internet import protocol


.. doctest::

    >>> someFactory = protocol.ServerFactory()
    >>> d = storedEndpoint.listen(someFactory)

.. toctree::
   :maxdepth: 2

   endpoints.rst
   credentials.rst
