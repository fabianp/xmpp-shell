XMPP-shell
==========

Remote shell that uses XMPP as transporting protocol. This makes it possible to access a remote computer using
an XMPP account.

Initial stage, just proof of concept.

Installation
============

    $ pip install -U xmpp-shell

How to use it
=============

First launch a service in the machine you will be connecting to so that it can accept sessions::

    $ xmpp-shell --server

To connect to that machine call xmpp-shell without the --server flag::

    $ xmpp-shell

and you will be presented with a list of available sessions (TODO).

Behind a firewall
=================

Some xmpp servers such as http://jabber80.com offer accounts on non-firewalled ports. You can open
an account on this server using XMPP clients such as Pidgin/Adium.

TODO
====

 - Control-C and q key (on daemon)
 - multiple sessions on the server
 - double authentication: on XMPP and on the host machine
 - Exception on wrong login (bug in sleekxmpp)


Development
===========

...

Author
======

Fabian Pedregosa <fabian@fseoane.net>

License
=======

New BSD