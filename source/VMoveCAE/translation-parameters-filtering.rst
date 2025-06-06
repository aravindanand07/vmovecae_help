Filtering Parts, Results and Instances in Translation Parameters Files
======================================================================
In VMoveCAE, parts, results and instances can be specified for filtering while using translation parameters files.  

**Translating and Filtering Parts**

Consider the below examples for text and XML file formats.

Text File::

        [translation]
            ...
             
            [part]
                name = cyl-wall-layer
                 
                id = 47
                translate = true
            []
             
            ...
        []


XML File::

        <translation>
            ... 
             
            <part> 
                <attribute key="name" value="cyl-wall-layer" />
                 
                <attribute key="id" value="47" />
                <attribute key="translate" value="true" />
            </part>
             
            ...
        </translation>
 


Note: 

-  	Users can specify either a name variable or an id variable for each part. 
  
-  For Ansys files,

   -  The name refers to the name of the named component in the ds.dat
      or cdb file.
   -  The id refers to the the element type number

-  For Fluent mesh and solution files,

   -  The name refers to the name or either a face zone or a cell zone
   -  The id refers to the id of the face zone or a cell zone.

-  If both name and id are specified, and if there is a conflict, VMoveCAE ignores the name and uses the id to identify the part. 
-  The "translate" variable can have either "true" or "false" as its
   value.
-  A "filter" variable can be used instead of the "translate" variable.
   Specifying "filter = true" is same as "translate = false" and
   vice-versa.
-  The "translate" or "filter" variables are not mandatory. If they are
   not specified, the default values are used.

**Translating and filtering results**

Text File::

        [translation]
            ...

            [result]
                name = Displacement

                translate = true
            []

            ...
        []


XML File::

        <translation>
            ...

            <result>
                <attribute key="name" value="Displacement" />

                <attribute key="translate" value="true" />
            </result>

            ...
        </translation>

Note:

-  User need to specify the name of the result
-  Either “translate” or “filter” variable can be used to specify whether to translate or filter the result. If they are not specified, the default values are used. 

**Specifying the default behaviour**

Text file::

        [translation]
            ...

            [defaults]
                parts = filter

                results = filter
            []

            ...
        []


XML File::

        <translation>
            ...

            <defaults>
                <attribute key="parts" value="filter" />

                <attribute key="results" value="filter" />
            </defaults>

            ...
        </translation>

Note:

-  The "parts" variable specify whether to filter or translate the
   unspecified parts
-  The "results" variable specify whether to filter or translate the
   unspecified results.
-  The valid values for the "parts" and "results" are "translate" and
   "filter".
-  If user specifies, "parts = translate" in the "defaults" block, the
   default value of "translate" for parts is taken as "false" and
   vice-versa.
-  Similarly, if user specifies, "results = filter" in the "defaults"
   block, the default value of the "translate" for the results is take
   as "true" and vice-versa.

