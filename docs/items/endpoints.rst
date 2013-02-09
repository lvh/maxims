Endpoints
=========

You can persist Twisted server and client endpoints. They are stored
and created using their string descriptions. You can create the
regular endpoint objects by calling their ``instantiate`` methods, but
the preferred API is to call ``listen`` or ``connect`` just as if they
were regular endpoints.

Examples
--------

Here's a server endpoint:

.. literalinclude::

    >>> serverEndpoint = endpoints.ServerEndpoint(description="tcp:0")
    >>> serverEndpoint.listen(someFactory)

Here's a client endpoint:

.. literalinclude::

    >>> clientEndpoint = endpoints.ClientEndpoint(description="tcp:www.google.com:80")
    >>> clientEndpoint.connect(someFactory)  
