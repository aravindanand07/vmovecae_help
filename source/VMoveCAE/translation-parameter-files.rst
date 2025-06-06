Translation Parameters Files and Their Structure
==================================================

In VMoveCAE, users can save the translation parameters in a file and use it  to create CAX files in batch mode. These translation parameters files can also be created manually or through VMoveCAE GUI.

The translation parameters files include the location of the model, results and CAX files, settings for different features as well as translation and filtering information of different parts, results and features. VMoveCAE supports both text and XML formatted translation parameters files. Sample translation parameters files in both text and XML format can be downloaded from the below links.

Download :download:`ic3d1000_translation_parameters.txt <ic3d1000_translation_parameters.txt>`

Download :download:`ic3d1000_translation_parameters.xml <ic3d1000_translation_parameters.xml>`


Once a translation parameters file is created it can be used in batch mode as shown below. 

**VMoveCAEBatch.exe -b <translation_parameters_file>**

**Translation parameters file structure**

-  The translation parameters file is comprised of hierarchically structured blocks.

-  Each block may in turn consists of inner blocks as well as a set of key and value pairs.

-  The outermost block should always be "VMoveCAE".

-  The "VMoveCAE" block consists of

  -  The translation parameters file version
  -  The parameters for one or more translations

Any thing followed by ' # ' is in the text file considered as a comment.

in XML files, comments can be embedded between "<!--" and "-->" 

::

          [VMoveCAE]
              version = 2.0     # current parameters file format version

              [translation]
                  # parameters for first translation

                  ...

              []
              [translation]
                  # parameters for first translation

                  ...

              []
          []

::

          <?xml version="1.0" encoding="iso-8859-1" ?>
          <VMoveCAE>
              <attribute key="version" value="2.0" />
               
              <translation>
                  <!-- parameters for first translation -->
                   
                  ...

              </translation>
               
              <translation>
                  <!-- parameters for first translation -->
                   
                  ...

              </translation>
              
          </VMoveCAE>

**Specifying the file paths**

Each translation block can specify a "model file", "results file" and an "output file". The syntax for specifying them in text file and XML file is shown below. 

Text File::

          [translation]
              model file = "D:\Samples\file.rst"
              output file = "D:\Samples\file.cax"
              
              # other parameters for first translation
              ...
              
              ...

          []
           
          [translation]
              model file = "D:\Samples\ic3d1000.cas"
              results file = "D:\Samples\ic3d1000.dat"
              output file = "D:\Samples\ic3d1000.cax"
               
              # other parameters for second translation
              ...

          []


 XML File::

      <translation>
          <attribute "model file" value="D:\Samples\file.rst" />
          <attribute key="output file" value="D:\Samples\file.cax" />

          <!-- other parameters for first translation -->  

          ...

          </translation>

          <translation>
          <attribute key="model file" value="D:\Samples\ic3d1000.cas" />
          <attribute key="results file" value="D:\Samples\ic3d1000.dat" />  
          <attribute key="output file" value="D:\Samples\ic3d1000.cax" />

          <!-- other parameters for second translation -->

          ...

          </translation>


Users can also specify the model, results and output files on the command line instead of the translation parameters files as shown below. If the model, results and output files are specified on the command line, the values specified in the translation parameters files are ignored as in the following example:

    **VMoveCAEBatch.exe -b translation_parameters.txt
    blower.cas blower.dat blower.cax**


