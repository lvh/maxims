Endpoints
=========

You can persist Twisted server and client endpoints. They are stored and created using their string descriptions.

.. testsetup::

    from maxims import endpoints

.. doctest::

    >>> storedEndpoint = endpoints.ServerEndpoint("tcp:0")
    >>> storedEndpoint.instantiate()
