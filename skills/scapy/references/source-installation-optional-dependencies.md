
    >>> enc=rdpcap("weplab-64bit-AA-managed.pcap")
    >>> enc.show()
    >>> enc[0]
    >>> conf.wepkey="AA\x00\x00\x00"
    >>> dec=Dot11PacketList(enc).toEthernet()
    >>> dec.show()
    >>> dec[0]
 
* PKI operations and TLS decryption. `cryptography <https://cryptography.io>`_ is also needed.

* Fingerprinting. ``nmap_fp()`` needs `Nmap <http://nmap.org>`_. You need an `old version <http://nmap.org/dist-old/>`_ (before v4.23) that still supports first generation fingerprinting.

  .. code-block:: python 
  
    >>> load_module("nmap")
    >>> nmap_fp("192.168.0.1")
    Begin emission:
    Finished to send 8 packets.
    Received 19 packets, got 4 answers, remaining 4 packets
    (0.88749999999999996, ['Draytek Vigor 2000 ISDN router'])
 
* VOIP. ``voip_play()`` needs `SoX <http://sox.sourceforge.net/>`_.

Platform-specific instructions
==============================

As a general rule, you can toggle the **libpcap** integration `on` or `off` at any time, using::

    from scapy.config import conf
    conf.use_pcap = True

Linux native
------------

Scapy can run natively on Linux, without libpcap.

* Install `Python 3.7+ <http://www.python.org>`__.
* Install `libpcap <http://www.tcpdump.org>`_. (By default it will only be used to compile BPF filters)
* Make sure your kernel has Packet sockets selected (``CONFIG_PACKET``)
* If your kernel is < 2.6, make sure that Socket filtering is selected ``CONFIG_FILTER``) 

Debian/Ubuntu/Fedora
--------------------

Make sure libpcap is installed:

- Debian/Ubuntu:

.. code-block:: text

    $ sudo apt-get install libpcap-dev

- Fedora:

.. code-block:: text

	$ yum install libpcap-devel

Then install Scapy via ``pip`` or ``apt`` (bundled under ``python3-scapy``)
All dependencies may be installed either via the platform-specific installer, or via PyPI. See `Optional Dependencies <#optional-dependencies>`_ for more information.


Mac OS X
--------

On Mac OS X, Scapy **DOES work natively** since the recent versions.
However, you may want to make Scapy use libpcap.
You can choose to install it using either Homebrew or MacPorts. They both
work fine, yet Homebrew is used to run unit tests with
`Travis CI <https://travis-ci.org>`_. 

.. note:: 
    Libpcap might already be installed on your platform (for instance, if you have tcpdump). This is the case of `OSX <https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/pcap.3.html>`_

Install using Homebrew
^^^^^^^^^^^^^^^^^^^^^^

1. Update Homebrew::

   $ brew update

2. Install libpcap::

   $ brew install libpcap

Enable it In Scapy::

    conf.use_pcap = True

Install using MacPorts
^^^^^^^^^^^^^^^^^^^^^^

1. Update MacPorts::

   $ sudo port -d selfupdate

2. Install libpcap::

   $ sudo port install libpcap

Enable it In Scapy::

    conf.use_pcap = True

OpenBSD
-------

In a similar manner, to install Scapy on OpenBSD 5.9+, you **may** want to install libpcap, if you do not want to use the native extension:

.. code-block:: text

	$ doas pkg_add libpcap

Then install Scapy via ``pip`` or ``pkg_add`` (bundled under ``python-scapy``)
All dependencies may be installed either via the platform-specific installer, or via PyPI. See `Optional Dependencies <#optional-dependencies>`_ for more information.

SunOS / Solaris
---------------

Solaris / SunOS requires ``libpcap`` (installed by default) to work.

.. note::
    In fact, Solaris doesn't support `AF_PACKET`, which Scapy uses on Linux, but rather uses its own system `DLPI`. See `this page <https://www.oracle.com/technetwork/server-storage/solaris/solaris-linux-app-139382.html>`_.
    We prefer using the very universal `libpcap` that spending time implementing support for `DLPI`.

.. _windows_installation:

Windows
-------

You need to install Npcap in order to install Scapy on Windows (should also work with Winpcap, but unsupported nowadays):

  * Download link: `Npcap <https://nmap.org/npcap/>`_: `the latest version <https://nmap.org/npcap/#download>`_
  * During installation:
      * we advise to turn **off** the ``Winpcap compatibility mode``
      * if you want to use your wifi card in monitor mode (if supported), make sure you enable the ``802.11`` option

Once that is done, you can `continue with Scapy's installation <#latest-release>`_.

You should then be able to open a ``cmd.exe`` and just call ``scapy``. If not, you probably haven't enabled the "Add Python to PATH" option when installing Python. You can follow the instructions `over here <https://docs.python.org/3/using/windows.html#finding-the-python-executable>`_ to change that (or add it manually).

Screenshots
^^^^^^^^^^^

.. image:: graphics/scapy-win-screenshot1.png
   :scale: 80
   :align: center

.. image:: graphics/scapy-win-screenshot2.png
   :scale: 80
   :align: center

Build the documentation offline
===============================

The Scapy project's documentation is written using reStructuredText (files \*.rst) and can be built using
the `Sphinx <http://www.sphinx-doc.org/>`_ python library. The official online version is available
on `readthedocs <http://scapy.readthedocs.io/>`_.

HTML version
