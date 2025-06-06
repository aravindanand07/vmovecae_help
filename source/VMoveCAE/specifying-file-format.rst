
Specifying File Format
======================

VMoveCAEBatch detects the file format of a CAE model file from its extension by default. To use a different file format instead of the format derived from the extension, command line argument **-\-model-file-format** can be used. 

Example:

VMoveCAEBatch.exe **-\-model-file-format="nastran_bdf" sample.dat sample.cax**

In the above example, the file format for sample.dat is explicitly specified as nastran_bdf. 

The supported file format names are listed below,

+------------------------+-----------------------------+-----------------------------+
| CAE files              |   File types                |     Explicit Specifications |
+========================+=============================+=============================+
| Nastran files          |       \*.bdf                |       nastran_bdf           |                     
|                        |                             |                             |
|                        |       \*.op2                |       nastran_op2           |       
|                        |                             |                             |
|                        |       \*. xdb               |       nastran_xdb           |        
+------------------------+-----------------------------+-----------------------------+
| Ansys files            |       \*.cdb                |       ansys_cdb             |                     
|                        |                             |                             |
|                        |       \*.rst                |       ansys_rst             |       
|                        |                             |                             |
|                        |       \*.rth                |       ansys_rth             |        
+------------------------+-----------------------------+-----------------------------+
| LSDyna files           |       \*.key                |       lsdyna_key            |                     
|                        |                             |                             |
|                        |       d3plot                |       lsdyna_d3plot         |       
|                        |                             |                             |        
+------------------------+-----------------------------+-----------------------------+
| Abaqus files           |       \*.inp                |       abaqus_inp            |                     
|                        |                             |                             |
|                        |       \*.fil                |       abaqus_fil            |       
|                        |                             |                             |
|                        |       \*.odb                |       abaqus_odb            |        
+------------------------+-----------------------------+-----------------------------+   
| Fluent files           |       \*.cas                |       fluent_cas            |                     
|                        |                             |                             |
|                        |       \*.cfx                |       cfx_res               |       
|                        |                             |                             |
|                        |       \*.ccm                |       starccm+_ccm          |        
+------------------------+-----------------------------+-----------------------------+                  
| IDEAS SDRC Universal   |       \*.unv                |       sdrc_unv              |                     
| files                  |                             |                             |                             
+------------------------+-----------------------------+-----------------------------+                          








             