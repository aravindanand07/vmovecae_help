Filtering Parts, Results and Instances in Batch Mode
=======================================================

In VMoveCAE, users can filter out parts, results and instances while translating a CAE file to a CAX file. This filtering can be achieved using command-line options as listed below. 

#. **--results=RESULT_LIST :** Translates the results listed in RESULT_LIST 

   Example: --results="Displacement, Stress" 

#. **--filter-results=RESULT_LIST :** Filters(excludes) the results specified in RESULT_LIST 

   Example: --filter-results="Von Mises Stress, Contact Pressure" 

#. **--parts=PART_LIST :** Translates the parts specified in PART_LIST 
  
   Example: --parts="HINGEBASE, BOLTSURF, _PICKEDSET8" 

#. **--filter-parts=PART_LIST :** Filters the parts specified in PART_LIST 

   Example: --filter-parts="_ALL ELEMENTS, WarnElemDistorted" 

#. **--parts-ids=PART_ID_LIST :** Translates the parts having ids listed in PART_ID_LIST 

   Example: --part-ids="1, 30-35, 41" 

#. **--filter-parts-ids=PART_ID_LIST :** Filters the parts having ids listed in PART_ID_LIST

   Example: --filter-part-ids="4-8, 12" 

#. **--instances=INSTANCE_LIST :** Translates the instances listed in INSTANCE_LIST 

   Example: --instances="1-6, 8-12" 

   Example: --instances="1:5-1:8, 2" 

#. **--filter-instances=INSTANCE_LIST :** Filters the instances listed in INSTANCE_LIST 

   Example: --filter-instances=":1-:4, 2" 

**Notes:**

   #. The value of each option is a list whose items are separated by commas. 
     
      For example, **--results="Displacement, Stress"** will translate results - "Displacement"              and "Stress".

   #. It is mandatory to enclose the list in quotes ("") when the list contains spaces.  The quotes can be avoided if there are no spaces.

      For example, **--results="Displacement, Stress"** and **--results=Displacement,Stress** are equivalent.  However, it is recommended to use quotes always. 

   #. The part ids as well as instances can have a hyphen to specify a range. 

      For example, **--filter-part-ids="4-8, 12"** option results in filtering of parts with ids 4, 5, 6, 7, 8 and 12. 

   #. The exact interpretation of **Instance** depends upon the context in which they are used. They are used in many places to signify the load step or time step number, increment number, vibration, or buckling mode number, etc. For example, for a CFD unsteady simulation, an instance 5 can represent fifth time-step in the simulation.   In an ABAQUS odb database the instance 3:2 is used to represent second frame of third step. 

   #. Multiple Hyphens ' - ' can be used together to specify the instances that need to be translated or filtered.  

      For Example:

      Option **--instances="1-6, 8-12"** specifies that instances one to six and eight to twelve needs to be translated.  

      Option **--instances="1:5-1:8, 2"** specifies that frames five to eight need to be translated for the first step along with all frames for the second step.

      Option **--filter-instances=":1-:4, 2"** filters out the frames from one to four for all steps.  It also filters out all the frames of the second step. 

   #. If both **--results** and **--filter-results** options are specified, the option **--filter-results** will be ignored. 

      When both **--instances** and **--filter-instances** options are specified,  **--filter-instances** option will be ignored. 

      When either **--parts** or **--part-ids** are specified, **--filter-parts** and **filter-part-ids** will be ignored.

   #. All the names of the results and parts are not case sensitive. 
