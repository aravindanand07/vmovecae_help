Enabling Mid-nodes for Translation
==================================

During translation to CAX files, VMoveCAE writes only the corner nodes values by default. The mid-nodes in higher order elements are not considered. This module shows how users can change the default setting to retain the mid-nodes in VMoveCAE GUI or batch mode. 

**VMoveCAE GUI**

   #. Start **VMoveCAE** and load a CAE file with mid-nodes.
  
   #. Go to **Settings->Preferences** to open the Preferences dialog box. Uncheck **Ignore mid-nodes** checkbox. 
  
        |Controlling_Mid_node|

   #. Click on the Save **CAX** icon to save the file. The output CAX file will contain the mid-nodes as desired.

**Batch Mode**

The translation of mid-nodes can be enabled in batch mode using the **“--enable-mid-nodes”** command line option.

.. |Controlling_Mid_node| image:: images/Controlling_Mid_node.png
  


    
