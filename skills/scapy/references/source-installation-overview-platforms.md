# Source: installation

.. highlight:: sh

*************************
Download and Installation
*************************

Overview
========

 0. Install `Python 3.7+ <https://www.python.org/downloads/>`_.
 1. `Download and install Scapy. <#installing-scapy-v2-x>`_
 2. `Follow the platform-specific instructions (dependencies) <#platform-specific-instructions>`_.
 3. (Optional): `Install additional software for special features <#optional-software-for-special-features>`_.
 4. Run Scapy with root privileges.
 
Each of these steps can be done in a different way depending on your platform and on the version of Scapy you want to use.  Follow the platform-specific instructions for more detail.

Scapy versions
==============

.. note:: Scapy 2.5.0 was the last version to support Python 2.7 !

+------------------+-------+-------+--------+
| Scapy version    | 2.3.3 | 2.5.0 | >2.5.0 |
+==================+=======+=======+========+
| Python 2.2-2.6   | ✅    | ❌    | ❌     |
+------------------+-------+-------+--------+
| Python 2.7       | ✅    | ✅    | ❌     |
+------------------+-------+-------+--------+
| Python 3.4-3.6   | ❌    | ✅    | ❌     |
+------------------+-------+-------+--------+
| Python 3.7-3.14  | ❌    | ✅    | ✅     |
+------------------+-------+-------+--------+

Installing Scapy v2.x
=====================

The following steps describe how to install (or update) Scapy itself.
Dependent on your platform, some additional libraries might have to be installed to make it actually work. 
So please also have a look at the platform specific chapters on how to install those requirements.

.. note::

   The following steps apply to Unix-like operating systems (Linux, BSD, Mac OS X). 
   For Windows, see the  `special chapter <#windows>`_ below.

Make sure you have Python installed before you go on.

Latest release
--------------

.. note::
   To get the latest versions, with bugfixes and new features, but maybe not as stable, see the `development version <#current-development-version>`_.

Use pip::

$ pip install scapy

..
    !! COMMENTED UNTIL NEXT RELEASE !!
    Scapy specifies ``optional-dependencies`` so that you can install its optional dependencies directly through pip:

    +----------+------------------------------------------+-----------------------------+
    | Bundle   | Contains                                 | Pip command                 |
    +==========+==========================================+=============================+
    | Default  | Only Scapy                               | ``pip install scapy``       |
    +----------+------------------------------------------+-----------------------------+
    | CLI      | Scapy & IPython. **Highly recommended**  | ``pip install scapy[cli]``  |
    +----------+------------------------------------------+-----------------------------+
    | All      | Scapy & all its optional dependencies    | ``pip install scapy[all]``  |
    +----------+------------------------------------------+-----------------------------+

 
Current development version
----------------------------

.. index::
   single: Git, repository

If you always want the latest version of Scapy with all new the features and bugfixes (but slightly less stable), you can install Scapy from its Git repository.

.. note:: If you don't want to clone Scapy, you can install the development version in one line using::

    $ pip install https://github.com/secdev/scapy/archive/refs/heads/master.zip

1. Check out a clone of Scapy's repository with `git <https://git-scm.com/book/en/v2/Getting-Started-Installing-Git>`_::

   $ git clone https://github.com/secdev/scapy.git
   $ cd scapy

2. Install Scapy using `pip <https://docs.python.org/dev/installing/index.html>`_:: 

   $ pip install .

3. If you used Git, you can always update to the latest version afterwards::

   $ git pull
   $ pip install .

.. note::

   You can run scapy without installing it using the ``run_scapy`` (unix) or ``run_scapy.bat`` (Windows) script.

Optional Dependencies
=====================

For some special features, Scapy will need some dependencies to be installed.
Most of those software are installable via ``pip``.
Here are the topics involved and some examples that you can use to try if your installation was successful.

.. index::
   single: plot()

* Plotting. ``plot()`` needs `Matplotlib <https://matplotlib.org/>`_.

  Matplotlib is installable via ``pip install matplotlib``
 
  .. code-block:: python
   
    >>> p=sniff(count=50)
    >>> p.plot(lambda x:len(x))
 
* 2D graphics. ``psdump()`` and ``pdfdump()`` need `PyX <http://pyx.sourceforge.net/>`_ which in turn needs a LaTeX distribution: `texlive (Unix) <http://www.tug.org/texlive/>`_ or `MikTex (Windows) <https://miktex.org/>`_.
  
  You can install pyx using ``pip install pyx``
  
  .. code-block:: python
   
    >>> p=IP()/ICMP()
    >>> p.pdfdump("test.pdf") 
 
* Graphs. ``conversations()`` needs `Graphviz <http://www.graphviz.org/>`_ and `ImageMagick <http://www.imagemagick.org/>`_.
 
  .. code-block:: python

    >>> p=rdpcap("myfile.pcap")
    >>> p.conversations(type="jpg", target="> test.jpg")

  .. note::
    ``Graphviz`` and ``ImageMagick`` need to be installed separately, using your platform-specific package manager.

* 3D graphics. ``trace3D()`` needs `VPython-Jupyter <https://github.com/vpython/vpython-jupyter/>`_.

  VPython-Jupyter is installable via ``pip install vpython``

  .. code-block:: python

    >>> a,u=traceroute(["www.python.org", "google.com","slashdot.org"])
    >>> a.trace3D()

.. index::
   single: WEP, unwep()

* WEP decryption. ``unwep()`` needs `cryptography <https://cryptography.io>`_. Example using a `Weplap test file <http://weplab.sourceforge.net/caps/weplab-64bit-AA-managed.pcap>`_:

  Cryptography is installable via ``pip install cryptography``

  .. code-block:: python
