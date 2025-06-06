Nodal Averaging Options
===========================

To compute nodal values from element nodes, VMoveCAE uses the averaging technique as shown in the figure. 

                            |Nodal_Averaging_Options|

                      Elemental nodal to nodal averaging process 

**Computing Nodal Averages from Elemental Node**

VMoveCAE follows the “average and derive” principle for computing the derived values of vector, six dof and tensor results. All the components are first computed at the nodes by averaging the element nodal values. These average nodal values are used to define the derived quantities.

**Disabling Nodal Averaging Across Materials** 

For computing nodal values, Ansys workbench considers nodes and elements of the same material only. Multiple nodal values are defined on the interfaces of materials during the nodal averaging process. Unlike Ansys workbench, VMoveCAE considers the nodes across materials by default while computing the nodal values from elemental or element location values. Due to this, the nodal average values and their ranges may differ in VMoveCAE and Ansys post-processor. 

Users can alter this default setting in VMoveCAE through the GUI or in batch mode.

**VMoveCAE GUI**

  #. Start **VMoveCAE** and load an input file.

  #. Go to **Settings->Preferences** to open the Preferences dialog box. Check **No averaging across materials** as shown below. 

          |Nodal_Averaging_Options_GUI| 

As a result of this setting, VMoveCAE preserves the discontinuities of values across the materials during the elemental to nodal and element nodal to nodal averaging processes. 

**Batch Mode**

The command to disable nodal averaging across materials in batch mode is **“--no-averaging-across-materials”**. The below example shows how to preserve material discontinuities while reading the geometry and results from **file.rst** and named components from **ds.dat** and translating them into **file.cax**. 

   VMoveCAEBatch.exe **--ansys-input-commands="ds.dat" --no-averaging-across-materials file.rst file.cax** 


.. |Nodal_Averaging_Options| image:: images/Nodal_Averaging_Options.png
.. |Nodal_Averaging_Options_GUI| image:: images/Nodal_Averaging_Options_GUI.png
  


    
