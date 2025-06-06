Files Section
=============

-  Used to specify the files that needs to be read and written by
   VMoveCAE

-  This is a mandatory section and must be available in the input file.

-  Usage Example:

   .. code-block::

      * FILES, FOLDER="/home/vcollab/models"

      - "viewer_tutorial.odb", TYPE=ABAQUS_ODB

-  The file path or file name for each of the input files should be
   provided in one data line as the name.

.. toctree::
   :maxdepth: 4
   :caption: File Attributes:

   section_attributes
   data_attributes




Examples & Description
----------------------

.. admonition::  Example 1 
   
   .. code-block::
   
      * FILES, FOLDER=/home/test/models
      - viewer_tutorial.odb
   -  Reads model and results from "viewer_tutorial.odb" file in the
      "/home/test/models" folder. File type and content type are
      identified automatically.
   -  Since no CAX file name is provided, output is written to
      "viewer_tutorial.cax" in the same folder.

.. admonition::  Example 2
   
   .. code-block::
   
      * FILES
      -  Linear-Job_modified.inp, TYPE=ABAQUS_INP, CONTENT=ENTITY_SETS
      -  Linear-Job_post.odb, TYPE=ABAQUS_ODB, CONTENT=“MODEL, RESULTS”
      -  Linear-Job_fatigue.dma, TYPE=FEMFAT_DMA, CONTENT=RESULTS
      -  Linear-Job.cax, TYPE=VCOLLAB_CAX
      -  vmovecae_trace.log, TYPE=VMOVE_LOG

   -  Reads model and results from "Linear-Job_post.odb" file in the current
      folder.
   -  Element sets are read from "Linear-Job_modified.inp" instead of the ODB
      file. The element ids should match in the INP and ODB files to get the
      correct output.
   -  Reads additional results from "Linear-Job_fatigue.dma" and appends them
      to the results in the ODB file.
   -  The output is written to the "Linear-Job.cax" file in the current folder.
   -  Translation log is written to "vmovecae_trace.log" file in the current
      current folder.

.. admonition::  Example 3
   
   .. code-block::
   
      * FILES

      -  Linear-Job.inp, TYPE=ABAQUS_INP, CONTENT=MODEL
      -  Linear-Job.dma, TYPE=FEMFAT_DMA, CONTENT=RESULTS
      -  Linear-Job.cax, TYPE=VCOLLAB_CAX
      -  vmovecae_trace.log, TYPE=VMOVE_LOG

   -  Reads the model "Linear-Job.inp" file in the current folder.
   -  Reads additional results from "Linear-Job.dma" and appends them
      to the model in the INP file.
   -  The output is written to the "Linear-Job.cax" file in the current folder.
   -  Translation log is written to "vmovecae_trace.log" file in the current
      current folder.

.. admonition::  Example 4
   
   .. code-block::
    
      * FILES

      -  viewer-tutorial.odb, TYPE=ABAQUS_ODB, CONTENT=“MODEL, RESULTS” ,
         OPTIONS=“ZERO_FRAMES”
      -  viewer-tutorial.cax, TYPE=VCOLLAB_CAX, OPTIONS=“MID_NODES”
      -  vmovecae_trace.log, TYPE=VMOVE_LOG

   -  Reads the model "viewer_tutorial.odb" file in the current folder.
   -  Since the ZERO_FRAMES option is specified, VMoveCAE reads and exports
      specified initial conditions corresponding to the frame number zero as
      well. When this is not specified, VMovecAE only reads frames starting with
      number `1`.
   -  The output is written to the "viewer-tutorial.cax" file in the current
      folder.
   -  The exported CAX file also contains the mid-nodes in the mesh. When this
   -  option is not specified, the mid-nodes are ignored and not exported into
      the mesh written into the CAX file.
   -  When the CAX file name is not explicitly specified, the MID_NODES option
      can be specified with the model file.
   -  Translation log is written to "vmovecae_trace.log" file in the current
      current folder.

.. admonition::  Example 5
   
   .. code-block::
   
      * FILES, MERGE_TYPE=STEPS

      -  modes_x.odb
      -  modes_x.dma
      -  modes_y.odb
      -  modes_y.dma
      -  modes_z.odb
      -  modes_z.dma
      -  modes.cax
      -  vmovecae_trace.log

   The resulting CAX file is equivalent to the CAX file created with the
   following two step process.

   **STEP 1**
     -  Create the first CAX file with the model and results from "modes_x.odb"
        and with the additional results from "modes_x.dma".
     -  Create the second CAX file with the model and results from "modes_y.odb"
        and with the additional results from "modes_y.dma".
     -  Create the third CAX file with the model and results from "modes_z.odb"
        and with the additional results from "modes_z.dma".

   **STEP 2**
     -  Merge the CAX files together and renumber the frames and increments to
        avoid the clashes.

   As mentioned earlier, the models should be exactly same in all the ODB files.

.. admonition::  Example 6
   
   .. code-block::
   
      * FILES, MERGE_TYPE=STEPS

      -  modes_sets.inp, CONTENT=ENTITY_SETS
      -  modes_x.odb
      -  modes_x.dma
      -  modes_y.odb
      -  modes_y.dma
      -  modes_z.odb
      -  modes_z.dma
      -  modes.cax
      -  vmovecae_trace.log

   This example is similar to the one in example 5. Only difference is that,
   the element sets are read from "mode_sets.inp" instead of the ODB files.

.. admonition::  Example 7
   
   .. code-block::
   
      * FILES, MERGE_TYPE=STEPS

     -  modes_x.odb
     -  modes_y.odb
     -  modes_z.odb
     -  modes_x.dma
     -  modes_y.dma
     -  modes_z.dma
     -  modes.cax
     -  vmovecae_trace.log

   This example is similar to the one in example 5 with the exception of the
   sequence of the result files. The sequence of the steps and frames in the
   resultant CAX file will change appropriately. The step and frame numbers
   for the results from the dma files appear at the end.

.. admonition::  Example 7
   
   .. code-block::

      * FILES
      - viewer_tutorial.odb
      - history-output.his, TYPE=VCOLLAB_HIST

   This example explains how to extract the history output data from Abaqus ODB file.

.. admonition:: Example 8

   .. code-block::

      * FILES
      - abc.t16, OPTIONS="MARC_NO_RIGID_SURFACES"

   Marc Experimental Features. Its a default value, To turn off, user can define MARC_NO_RIGID_SURFACES option

.. admonition:: Example 8

   .. code-block::

      * FILES
      - ds.dat, TYPE=ANSYS_CMDS
      - file.rst

   

.. admonition:: Example 8

   .. code-block::
      
      * FILES
      - blower.cas, TYPE=FLUENT_CAS
      - blower.dat, TYPE=FLUENT_DAT

   This example explains how to load FLUENT_CAS (.cas) model and appending FLUENT_DAT (.dat) files.