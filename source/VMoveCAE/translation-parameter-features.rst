Specifying and Creating Features in Translation Parameters File
===============================================================
Features can be specified and created in translation parameters file.

**Specifying Cut-sections in Text and XML formats**

Text File::

        [translation]
            ...

            [cut-section]
                plane equation = "2.4X+0.6Y-3.2Z=20.6"

            []

            ...
        []

XML File::

        <translation>
            ...

            <cut-section>
                <attribute key="plane equation" value="2.4X+0.6Y-3.2Z=20.6" />
            </cut-section>

            ...
        </translation>

Note:

-  User need to specify the "plane equation" in the form of "AX+BY+CZ=D"
   form. 
-  All the cut-sections specified in the translation parameters files are created by default.  To skip the creation of cut-sections, users need to specify “translate = false”.  The default value of the “translate” variable is “true” for cut-sections. 
   is "true" for cut-sections.

**Specifying Iso-surfaces in Text and XML formats**

Text File::

        [translation]
            ...

            [iso-surface]
                result = "Stress"
                derived type = "Von Mises"

                value = 2400
            []

            ...
        []

XML File::

        <translation>
            ...

            <iso-surface>
                <attribute key="result" value="Stress" />
                <attribute key="derived type" value="Von Mises" />

                <attribute key="value" value="2400" />
            </iso-surface>

            ...
        </translation>

Note:

-  The result variable is mandatory
-  Derived types that need to be used when the result is non-scalar can also be specified. The default derived type for a vector is the magnitude of the vector. The default derived type for a stress tensor is the Von Mises stress. 
-  All the iso-surfaces specified in the translation parameters files are created by default.  To skip the creation of iso-surfaces, users need to specify “translate = false”.  The default value of the “translate” variable is “true” for iso-surfaces.

**Specifying Flow-lines in Text and XML formats**

Text File::

        [translation]
            ...

            [field-line]
                result = "Velocity"
                from = "inlet"

                number of lines = 50
            []

            ...
        []


XML File::

        <translation>
            ...

            <flow-line>
                <attribute key="result" value="Velocity" />
                <attribute key="from" value="inlet" />

                <attribute key="number of lines" value="50" />

            </flow-line>

            ...
        </translation>


Note:

-  The "result" variable is mandatory.
-  “From” variable is used to specify the location of the seed points.  Seed points should be defined in the (X, Y, Z) form or as a part name that can be used as the origin of seed points.   
-  The “number of lines” variable is used only when a part name is defined as the origin for the seed points.  The default value for the “number of lines” is 0.  VMoveCAE computes the number of seed points in this case automatically. 
-  The seed points are distributed randomly at present. 
-  All the flow-lines specified in the translation parameters files are created by default. To skip the creation of flow-lines, users need to specify “translate = false”.  The default value of the “translate” variable is “true” for flow-lines.

