Element Grouping and Parts
=============================================

**Parts Classification in VMoveCAE**

In VMoveCAE, the basis for parts classification is different for different file formats.  The following table lists the various file formats and their corresponding parts classification.

==============================================   ====================================
 **File Format**                                   **Part Classifier**
==============================================   ====================================
 LS-Dyna input decks and binary result data      Material identifier
 ANSYS solution files                            Element type number
 ABAQUS input decks and results                  Element set name
 MSC.NASTRAN input decks and results files       Identifier
 MSC.MARC results                                Element sets and contact sets
 Fluent mesh and case files                      Zone identifier
 StarCCM+ results                                Region identifier

==============================================   ====================================



**Changing the Element Grouping**

  Users can change the element grouping and part generation through GUI or in batch mode.  

**VMoveCAE GUI**

   #. Start **VMoveCAE** and load a CAE file.
  
   #. Go to **Settings->Preferences** to open the Preferences dialog box. 

   #. Click on **Part Grouping**. Select the **Part Grouping Type** for all the required interfaces and click “OK” to save these preferences to VMoveCAE GUI configuration file.  

    |element_Grouping_and_Parts|


**Note:** Clicking on **Reset** clears the interface changes made in that session. Clicking on **Defaults** resets the part grouping to VMoveCAE default for all the interfaces.

**Batch Mode**

Users can specify the element grouping mechanism for generating parts using the **“--part-grouping”** command line option. The supported grouping types are listed below.  

==============================================   ====================================
 **Element Group Type**                                 **Description**
==============================================   ====================================
 default                                         Use default part generation mechanism
 property-id                                     Use property id or ODB sections to group elements into 
                                                 parts
 material-id                                     Use material id to group elements into parts

 element-set                                     Use element sets to create parts

 element-type-number                             Use element type and number to group elements into parts

 no-parts                                        No parts to be created
==============================================   ====================================

For example, to create parts based on **property-id** element group the command to be used is: 


       **VMoveCAEBatch.exe --part-grouping="property-id" hinge.odb hinge.cax**

Similar commands can be used for other element group types (material-id, element-set, etc) to generate parts.

.. |element_Grouping_and_Parts| image:: images/element_Grouping_and_Parts.png
  


    
