Appending Results from CSV File
=================================

VMoveCAE supports appending nodal and elemental results from CSV files for **bdf** and **inp** models. 

**Points to Note:**


   #. Files with extension .csv or .csvn are treated as nodal result files and those with an extension of .csve 
      are treated as elemental results.
 
   #. VMoveCAE looks for the results name in the first line i.e the header of the file.  If the header is 
      missing, VMoveCAE automatically assigns the result names (e.g., Result1, Result2, etc).  Result names 
      should not contain any space.

   #. The first column of the CSV file should have the nodal or elemental (for .csve files) ids.

   #. Columns and results should be separated by spaces or tabs and not commas.