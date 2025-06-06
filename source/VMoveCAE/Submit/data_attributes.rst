Data Attributes
===============

**1. TYPE**

   To define the File type. Supported files are
   
   - CAE Model and Result Files
      
      - ABAQUS_ODB (.odb)
      - ANSYS_RST (.rst)
      - ANSYS_RTH (.rth)
      - NASTRAN_OP2 (.op2)
      - NASTRAN_XDB (.xdb)
      - NASTRAN_H5 (.h5)
      - LSDYNA_D3PLOT (d3plot* or .ptf)
      - ABAQUS_FIL (.fil)
      - MARC_T16 (.t16)
      - MARC_T19 (.t19)
      - CREO_SIMULATE
      - CFX_RES (.res)
      - STARCCM_CCM (.ccm)
      - CGNS (.cgns)
      - ENSIGHT_GOLD (.case, .encas)
      - OPENFOAM (controlDict)
      - TECPLOT_PLT (.plt)
      - OPTISTRUCT_H5 (.h5)
      - STL (.stl)
   - CAE Models
      - ABAQUS_INP (.inp)
      - ANSYS_CDB (.cdb)
      - NASTRAN_BDF (.bdf)
      - LSDYNA_KEY (.k, .key, .dyn)
      - FLUENT_CAS (.cas)
      - ANSYS_CMDS (ds.dat)
   - Result Files (Appendable)
      - FLUENT_DAT
         Appendable only to Fluent cas files. Default extension is not defined. User has to define the file type mandatorily.
         The .dat is regularly used for various file formats and may bring unnecessary confusion if we define it as the default extension.
      - FEMFAT_DMA (.dma, .univ)
      - VCOLLAB_CSV (.csv)
      - NUMPY_NPZ (.npz)
   - Output Files
      - VCOLLAB_CAX (.cax)
      - VCOLLAB_HIST (.his)
      - VMOVE_LOG (.log)
      - VCOLLAB_MT (.mt)


   **GuideLines to define TYPE**

   - **VMoveCAESubmit can deduct the file types for most formats:** 
      VMoveCAESubmit automatically determines the file type based on the file name and extension. The table above lists supported file names, extensions, and their corresponding file types.
   - **Avoid manual specification of file types whenever standard extensions are used:**
      It is generally recommended to avoid specifying file types manually in parameter files to prevent errors caused by typos.
   - **When to Specify File Types Explicitly?**
      - **Ambiguous Extensions:** Multiple solvers use the same file extension in their solution files. In such cases, user needs to specify the file type to avoid ambiguty.

         Example: Both ANSYS command files (ds.dat) and Fluent solution data files (.dat) use the same extension.
         By default, .dat is identified as an ANSYS command file. To use a Fluent solution data file, users must
         explicitly specify the type as FLUENT_DAT to avoid it being recognized as Ansys commands file.
      - **Non-Standard Extensions:** If a file has a non-standard extension, you must specify the file type.

         Example: Some NASTRAN users name bulk data files with .dat. Since only .nas and .bdf are recognized as
         Nastran bulk data files, users need to explicitly specify the file type as NASTRAN_BDF in such cases.

   
.. list-table:: Supported File Types
   :widths: 25 20 15 25 15
   :header-rows: 1

   * - File Name
     - Deducted File Type
     - Input/Output
     - What is Read/Written?
     - Requires Explicit Type
   * - .inp
     - ABAQUS_INP
     - Input
     - Model
     - No
   * - .cdb
     - ANSYS_CDB
     - Input
     - Model
     - No
   * - .bdf, .nas
     - NASTRAN_BDF
     - Input
     - Model
     - No
   * - .k, .key, .dyn
     - LSDYNA_KEY
     - Input
     - Model
     - No
   * - .odb
     - ABAQUS_ODB
     - Input
     - Model, Results
     - No
   * - .rst
     - ANSYS_RST
     - Input
     - Model, Results
     - No
   * - .rth
     - ANSYS_RTH
     - Input
     - Model, Results
     - No
   * - .op2
     - NASTRAN_OP2
     - Input
     - Model, Results
     - No
   * - .xdb
     - NASTRAN_XDB
     - Input
     - Model, Results
     - No
   * - .h5
     - NASTRAN_H5
     - Input
     - Model, Results
     - No
   * - .h5
     - OPTISTRUCT_H5
     - Input
     - Model, Results
     - No
   * - d3plot*, .d3plot, .d3eigv*, .d3eigv, .ptf
     - LSDYNA_D3PLOT
     - Input
     - Model, Results
     - No
   * - .fil
     - ABAQUS_FIL
     - Input
     - Model, Results
     - No
   * - .t16
     - MARC_T16
     - Input
     - Model, Results
     - No
   * - .T19
     - MARC_T19
     - Input
     - Model, Results
     - No
   * - .neu, .rpt
     - CREO_SIMULATE
     - Input
     - Model, Results
     - No
   * - .cas
     - FLUENT_CAS
     - Input
     - Model
     - No
   * - .res
     - CFX_RES
     - Input
     - Model & Results
     - No
   * - .ccm
     - STARCCM_CCM
     - Input
     - Model & Results
     - No
   * - .cgns
     - CGNS
     - Input
     - Model & Results
     - No
   * - .case, .encas
     - ENSIGHT_GOLD
     - Input
     - Model & Results
     - No
   * - controlDict
     - OPENFOAM
     - Input
     - Model & Results
     - No
   * - .plt
     - TECPLOT_PLT
     - Input
     - Model & Results
     - No
   * - .stl
     - STL
     - Input
     - Model
     - No
   * - .dat
     - FLUENT_DAT
     - Input
     - Results
     - Yes
   * - .dma, .univ
     - FEMFAM_DMA
     - Input
     - Results
     - No
   * - .dat
     - ANSYS_CMDS
     - Input
     - Component Names, Element Sets
     - No
   * - .csv
     - VCOLLAB_CSV
     - Input
     - Results
     - No
   * - .npz
     - NUMPY_NPZ
     - Input
     - Results
     - No
   * - .cax
     - VCOLLAB_CAX
     - Output
     - Cax
     - No
   * - .log
     - VMOVE_LOG
     - Output
     - VMoveCAE Translation Log
     - No
   * - .his
     - VCOLLAB_HIST
     - Output
     - History Data
     - No
   * - .mt
     - VCOLLAB_MT
     - Output
     - Mode Tables
     - No


**2. CONTENT**

   Tells VMoveCAE what to read/write from/to specific file.

   -  Supported file content types are:

      -  MODEL
      -  ENTITY_SETS
      -  RESULTS
      -  CAX
      -  LOG
   -  If not specified, VMoveCAE tries to identify it automatically.




**3. OPTIONS**

   Specify the file specific load and translation options.
   Supported options are:

   -  ZERO_FRAMES - Instructs VMoveCAE to load zero numbered frames (
      frames corresponding to the input conditions).
   -  FAST_LOAD - Instructs VMoveCAE to load assume that all the frames
      in the ODB file have same results. This allows VMoveCAE to load
      the ODB files faster.
   -  MID_NODES - Instructs VMoveCAE to extract the mid-nodes and the
      corresponding results into the CAX file.
   -  NO_AVERAGING_ACROSS_REGIONS - Instructs VMoveCAE to average
      element and element nodal results within regions boundaries only
      to obtain the nodal results. Please note that this has option has
      many limitations. For example, element results are not supported
      when this option is on. When not supported, the application falls
      back on regular averaging.
   -  CACHE_INPUT_FILES - local caching of input files.
   -  MARC_NO_RIGID_SURFACES - By default, the application reads RIGID surfaces from MARC files.
      To turn off, define this option.
   -  NODAL_AVERAGED_LOADS - Averaging loads at Nodes.