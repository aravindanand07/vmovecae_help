Caching Remote Input Files to Local Directory
=============================================

Large input files located in remote drives can be cached to a local folder to speed up loading and translation in VMoveCAE. This can be done by setting VCOLLAB_TEMP_PATH environment variable appropriately through VMoveCAE GUI or batch mode.

**VMoveCAE GUI**

   #. Start **VMoveCAE** and load a remote CAE file.
  
   #. Open the **Preference** dialog box (Settings->Preferences) and check **"Cache input files to temporary files folder"** option. 

    |local_Caching_of_Input_Files|

   #. Click on the "**OK**" button to update the setting. Input files of the
      future runs will be cached into a local folder before reading.


**Batch Mode**

The caching of files to temporary file folder can be enabled in batch mode using the ``--enable-input-files-caching``
command line option as shown in the following example.

.. code-block:: bash

       VMoveCAEBatch.exe --enable-input-files-caching hinge.odb hinge.cax

.. |local_Caching_of_Input_Files| image:: images/local-caching-of-input-files.png
  


    
