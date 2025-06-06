Section Attributes
===================

**1. FOLDER**

   -  When a base folder is specified, all the relative paths are
      considered to be relative to the base folder.
   -  Default value: Current working directory

**2. MERGE_TYPE**

   -  Tells VMoveCAE how to merge CAX files in the case of reading
      multiple model files.
   -  Default value: None. If not specified, VMoveCAE assumes that user
      is not trying merge results from different model files.
   -  This option should be specified if the user is trying to results
      from multiple model files.
   -  Supported values are:

      -  STEPS: Merge as steps of the same model.

   -  The sequence of the steps in the CAX file depends upon the
      sequence of results files. > **Note**: Please note that, only one
      option (``STEPS``) is supported as of now. It means that all the
      model files that are specified as input should have the same mesh,
      properties, element and face sets. The application doesn’t check
      this, and this validation should be done by the user. In the case
      that, this condition is not true, the resulting CAX file may get
      corrupted and users may not be able to open and visualize it.

**3. RETAIN_INTERMEDIATE**

   -  Tells VMoveCAE to retain the intermediate CAX files in the case of
      multiple model files.
   -  Valid only if MERGE_TYPE is specified. Ignored in other cases.
   -  Default value: False