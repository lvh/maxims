Items
=====

Items are just commonly reusable Axiom items. They can represent objects such as credentials, endpoints...

API
---

Things that can be persisted as Axiom items share a common API. The item has an ``instantiate`` method taking no arguments, giving you a new, independent instance of the object represented by that item.

.. testsetup::

    from maxims import endpoints

.. doctest::

    >>> storedEndpoint = endpoints.ServerEndpoint("tcp:0")
    >>> storedEndpoint.instantiate()

.. toctree::
   :maxdepth: 2

   endpoints.rst
   credentials.rst
