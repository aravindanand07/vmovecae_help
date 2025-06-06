CaeInfo in Batch Mode
=====================
VMoveCAE installation folder contains a console application **CaeInfo.exe** for generating and displaying metadata from native CAE files in XML format.  This metadata information includes parts and element sets defined in the CAE simulation file as well as the available results.  The metadata is displayed on the screen by default.  The syntax for using CaeInfo is:

**CaeInfo [options] <model_file> [results_file]**

Options:

**--output="file_name.xml" :** Writes the CAE file metadata to
the file_name.xml file

**Examples:**

#. The below example extracts the metadata from the d3plot file in the airbag folder.  This information is written to the console in XML format. 

   CaeInfo "models/ls-dyna/airbag/d3plot"

#. Instead of displaying it to the screen, an output file can be specified using the "--output" option. This example generates a metadata.xml file in the airbag folder with metadata from d3plot files. 

    CaeInfo "models/ls-dyna/airbag/d3plot" --output="models/ls-dyan/airbag/metadata.xml"

#. To provide results file for fluent simulations the command to be used is: 

   CaeInfo "models/fluent/ic3d1000.cas" "models/fluent/ic3d1000.dat"

Sample metadata files that are generated from CaeInfo.exe are available in the Samples folder of VCollab installation directory for user’s reference.
