Parts Section
=============

-  Used to specify VMoveCAE how to group elements into parts, what parts
   to translate and what parts to filter.

-  This is an optional section.

-  Each data line should contain the name of one part that needs to be
   translated or filtered.

-  Users can use ``*`` as a wildcard character.

-  Usage Example:

   .. code-block::

      * PARTS, GROUPING=element-set

      - PART-1-1_PLATE
      - CLAMP
      - HB*
      - STD*, FILTER  

Section Attributes
------------------

-  **GROUPING**: Part grouping to be used.

   -  Supported values:

      - property-id
      - material-id
      - element-set
      - face-set
      - element-and-face-sets
      - element-type-number
      - Element-types-and-components
      - fea-type
      - no-parts
      - ansa-part
      - hypermesh-components
      - ansys-bodies

   -  Default value: If part grouping is not specified, VMoveCAE uses
      default part grouping based on the file type. The default part
      grouping for different file formats is specified in the following
      table.

   ============================= =====================
   File Type                     Default Part Grouping
   ============================= =====================
   ABAQUS_ODB                    element-set
   ABAQUS_INP                    property-id
   CREO SIMULATE(.rpt)           Materials
   ENSIGHT CASE(.case, .encase)  Cell Zones
   NASTRAN (.bdf)                Properties
   ControlDict                   CellZones, FaceZones
   FLUENT                        CellZones, FaceZones
   CGNS                          CellZones
   LSDYNA                        Materials
   ANSYS_RTH                     Element Types
   ABAQUS_FIL                    Element sets
   SIEMENS_STARCCM               CellZones, FaceZones
   ANSYS CFX (.res)              CellZones, FaceZones
   MARC_POST                     Element Types, Contact Bodies
   NASTRAN_XDB                   Properties
   NASTRAN_OP2                   Properties
   ANSYS_CDB                     Element Types
   ANSYS_RST                     Element Types
   TECPLOT_PLT                   CellZones
   STEREO_STL                    Properties
   ============================= =====================
 
 
 

Data Attributes
---------------

-  **TRANSLATE**: Translates the part from Cax output. This is the
   default behavior.
-  **FILTER**: Filters the part from Cax output.

Examples & Description
----------------------

.. admonition:: Example 1
   
   .. code-block::
   
      * PARTS, GROUPING=element-set

      -  PART-1-1_PLATE
      -  CLAMP
      -  HB*

   Creates parts in CAX files based on the element sets in the model file.
   The resulting CAX file will contain the following parts.
   
   -  PART-1-1_PLATE
   -  CLAMP
   -  All element sets whose name starts with HB.

.. admonition:: Example 2

   .. code-block::
   
      * PARTS, GROUPING=property-id

      -  ASSEMBLY_PART-1-1_LING1, FILTER
      -  ASSEMBLY_PART-1-1_TRACE1, FILTER
      -  *SOIL*, FILTER

   Creates parts in CAX files based on the property ids (sections in Abaqus
   ODB files) in the model. The resulting CAX file will contain all the sections
   as parts except for the following.
   
   -  ASSEMBLY_PART-1-1_LING1
   -  ASSEMBLY_PART-1-1_TRACE1
   -  All sections with SOIL inside the name.
