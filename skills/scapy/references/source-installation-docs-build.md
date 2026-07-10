------------
The instructions to build the HTML version are: ::

   (activate a virtualenv)
   pip install sphinx
   cd doc/scapy
   make html

You can now open the resulting HTML file ``_build/html/index.html`` in your favorite web browser.

To use the ReadTheDocs' template, you will have to install the corresponding theme with: ::

   pip install sphinx_rtd_theme

UML diagram
-----------
Using ``pyreverse`` you can build a UML representation of the Scapy source code's object hierarchy. Here is an
example of how to build the inheritance graph for the Fields objects : ::

   (activate a virtualenv)
   pip install pylint
   cd scapy/
   pyreverse -o png -p fields scapy/fields.py

This will generate a ``classes_fields.png`` picture containing the inheritance hierarchy. Note that you can provide as many
modules or packages as you want, but the result will quickly get unreadable.

To see the dependencies between the DHCP layer and the ansmachine module, you can run: ::

   pyreverse -o png -p dhcp_ans scapy/ansmachine.py scapy/layers/dhcp.py scapy/packet.py

In this case, Pyreverse will also generate a ``packages_dhcp_ans.png`` showing the link between the different python modules provided.
