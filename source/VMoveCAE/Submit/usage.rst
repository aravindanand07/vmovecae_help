Usage
=====

-  VMoveCAE releases 21.6 onwards provide two new executables.

   -  VMoveCAEValidate: Checks the validity of the input file
   -  VMoveCAESubmit: Executes the application to generate CAX file
      according to the parameters specified in the input file.

-  They take a single argument file consisting of all the translation
   parameters as the input argument.

On Windows & Linux
------------------

-  VMoveCAEValidate inputs.txt
-  VMoveCAESubmit inputs.txt

On Linux
--------

In addition to these above commands, Linux installations also provide a
vmovecae shell script to their users. This shell script allows its users
to set the required executable and library paths, environment variables
and invoke the appropriate executables. VMoveCAEValidate and
VMoveCAESubmit can be invoked using this shell as shown below.

-  vmovecae -validate inputs.txt
-  vmovecae -submit inputs.txt
