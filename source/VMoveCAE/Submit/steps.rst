Steps Section
=============

-  Used to specify the steps/frames/load cases/modes that needs to be
   translated or filtered by VMoveCAE.

-  This is an optional section.

-  If not specified, VMoveCAE exports all the steps into CAX file.

-  Step numbers are specified in the data lines.

-  A range can be be specified using ``:`` as a separator.

-  ``-1`` can be used to refer to the last step.

-  ``ALL`` refers to all the available steps.

-  Usage Example:

   ::

      * STEPS

      - STEP=1, INCREMENT=2
      - STEP=1, INCREMENT=5:25:5
      - STEP=2, INCREMENT=ALL
      - STEP=3:-1, INCREMENT=-1

Data Attributes
---------------

-  **STEP**: Step numbers are specified in the data lines. A range can
   be be specified using ``:`` as a separator. ``-1`` can be used to
   refer to the last step. ``ALL`` refers to all the available steps.
-  **INCREMENT**: Increment number of the step to translate. A range can
   be specified using ``:`` as a separator. ``-1`` can be used to refer
   to the last increment. %- **TIME**: Time of the step/frame that needs
   to be translated. %- **FREQUENCY**: Frequency of the step/frame that
   needs to be translated.

Examples & Description
----------------------

.. admonition:: Example 1

   .. code-block::
   
      * STEPS

      -  STEP=1, INCREMENT=2
      -  STEP=1, INCREMENT=5:25:5
      -  STEP=2, INCREMENT=ALL
      -  STEP=3:-1, INCREMENT=-1

   The resulting CAX file will contain the following steps.
   
   -  Step 1, increments 2, 5, 10, 15, 20 and 25.
   -  All increments of step 2.
   -  The final increment for steps 3 to the final step.

.. admonition:: Example 2

   .. code-block::
   
      * STEPS

      -  STEP=2:4, INCREMENT=1:10, FILTER

   The resulting CAX file will contain all the steps in the given model
   and results files except for the increments 1 to 10 in steps 2 to 4.
