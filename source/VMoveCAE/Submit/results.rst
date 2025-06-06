Results Section
===============

-  Used to specify the results that needs to be translated or filtered
   by VMoveCAE.

-  This is an optional section.

-  If not specified, VMoveCAE exports all the results with the default
   settings into CAX file.

-  Each data line should contain the name of the result that needs to be
   translated or filtered.

-  Alternately, users can specify the source result name in the native
   CAE solver instead of using VCollab result name.

-  Wildcard character ``*`` is supported.

-  Unlike *Parts* and *Steps*, the *Results* section provides the
   functionality to allow the users to export the same result multiple
   times into CAX files each time with different settings.

-  Usage Example:

   ::

      * RESULTS

      - Displacement, SOURCE=U  
      - NT  
      - S, DERIVED=VON_MISES, THRESHOLD=75  
      - Elemental Stress, SOURCE=S, POSITION=E  

Section Attributes
------------------

-  **UNSPECIFIED**: Allows user to specify Whether to translate or
   filter the unspecified parts. It’s default value is false,
   i.e. unspecified results are not exported into CAX file.

Data Attributes
---------------

-  **TRANSLATE**: Translates the specified results. This is the default
   behavior.

-  **FILTER**: Filters the result from Cax output.

-  **SOURCE**: Name of the variable in the source CAE solver. Supported
   source values are: :ABAQUS_ODB: U, S, E, PE, PEEQ, LE, THE, NT, NT11,
   NT12, AC_YIELD, VEEQ, CPRES, CNORMF, CSHEAR1, CSHEAR2, CSHEARF,
   COPEN, CSLIP1, CSLIP2

-  **POSITION**:

   -  Instructs VMoveCAE whether to export nodal (N) or elemental (E)
      values.
   -  Nodal values are exported by default.
   -  For elemental results and for results that are defined at
      integration points, the nodal averaged values are exported.

-  **MAPTYPE**: Determines how the nodal values are computed from
   element/integration point values. Supported values:

   -  *GEOAVG*: Nodal values are computed by using geometry weights (
      area/volume) for the connected elements. This is the default
      value.
   -  *AVG*: Nodal values are computed by averaging the connected
      element values.
   -  *MAX*: Nodal values are taken as the maximum of the connected
      element values.
   -  *MIN*: Nodal values are taken as the maximum of the connected
      element values.

-  **SECTION**: Defines the sections to extract when values are defined
   for multiple sections.

   -  Shell, beam and membrane elements contain multiple values per
      element defined at different sections.
   -  User can define the sections for which the values that needs to be
      extracted using this option.
   -  Supported values:

      -  *TOP*: Top section values.
      -  *BOTTOM*: Bottom section values.
      -  *MAX*: Maximum of all sections.
      -  *MIN*: Maximum of all sections.
      -  *AVG*: Average of all sections.

   -  Default value: "TOP, BOTTOM"

-  **DERIVED**: Derived component that needs to be extracted.

   -  When this option is not specified, VMoveCAE exports the full
      vector/sixdof/tensor into the CAX file. The derived types are
      computed from the averaged component values.
   -  Specifying the *DERIVED* value makes VMoveCAE compute the derived
      types before averaging.
   -  Supported values:

   =========== =============
   Result Type Derived Types
   =========== =============
   Vector      X
   \           Y
   \           Z
   \           MAGNITUDE
   Tensor      XX
   \           YY
   \           ZZ
   \           XY
   \           YZ
   \           XZ
   \           VON_MISES
   \           MAX_PRINCIPAL
   \           MIN_PRINCIPAL
   \           MID_PRINCIPAL
   =========== =============

-  **THRESHOLD**: Percentage of averaging threshold to be used during
   the nodal value computations.

   -  Abaqus nodal value computations use a threshold percentage to
      identify discontinuities and determine whether to use averaged
      values or retain non-averaged values.
   -  This option serves similar purpose.
   -  The averaged value is retained only when range of weighted nodal
      value range is less than the threshold for the whole region.
   -  This option is valid only when the derived type is specified. It
      is ignored otherwise.
   -  Default value: 100%

-  **BTR_TYPE**: Tells VMoveCAE to retain the max/min value when the
   averaged nodal value is more than the threshold value.

   -  CAX files can retain only one value per node.
   -  When the weighted nodal value range is beyond the threshold value,
      user can specify VMoveCAE to retain the *MAX* or *MIN* value for
      that node.
   -  Default value: *MAX*.

Examples & Description
----------------------

.. admonition:: Example 1

   .. code-block::
   
      * RESULTS
      
      -  U
      -  S
      -  NT

   -  Exports displacement, temperature and stress to the CAX file.
   -  All other resulted are ignored.

.. admonition:: Example 2

   .. code-block::
   
       * RESULTS, UNSPECIFIED=TRANSLATE

       -  COPEN, FILTER
       -  CPRES, FILTER

   -  Filters contact opening and contact pressure.
   -  Exports all other results to CAX file.

.. admonition:: Example 3

   .. code-block::
   
     * RESULTS

     -  U
     -  S
     -  S, DERIVED=VON_MISES, THRESHOLD=75
     -  E, DERIVED=VON_MISES, THRESHOLD=75, BTR_TYPE=MIN

   -  Exports displacement and stress to CAX file.
   -  Two stress results are written into CAX file.
   -  Averaged stress component values are computed at the nodes and
      the full stress tensor is exported into the CAX file.
   -  The CAX file will also contain the Von Mises stress values computed
      at the nodes with an averaging threshold of 75%. For the nodes with
      ratio of the range is beyond the threshold value, maximum values of
      stress are exported.
   -  Von Mises strain values also get exported into the CAX file. For the
      nodes with ratio of the range is beyond the threshold value, minimum
      values are exported.
   -  Other results are filtered out and not exported into the CAX file.

.. admonition:: Example 4

   .. code-block::
   
      * RESULTS, UNSPECIFIED=TRANSLATE

      -  S, DERIVED=XX, THRESHOLD=75
      -  S, DERIVED=VON_MISES, THRESHOLD=75

   -  Exports all the results into CAX files.
   -  None of the results are filtered.
   -  Two stress results are exported. The first one is the X-component of
      stress with 75% averaging and the second one is the Von Mises stress
      with 75% averaging.
   -  Other results are exported with the default settings.

.. admonition:: Example 5

   .. code-block::
   
      * RESULTS, UNSPECIFIED=TRANSLATE

      -  S, POSITION=E

   -  Exports all the results into the CAX file.
   -  Exports elemental stresses and not nodal stresses.
   -  Other results are exported with the default settings.

.. admonition:: Example 6

   .. code-block::
   
      * RESULTS

      -  U
      -  S, DERIVED=XX, SECTION=MAX

   -  Displacements are exported into the CAX file.
   -  X-Components of the stress are exported with the 100% threshold averaging
      value. Maximum value across all sections are exported.
   - Other results are ignored.
