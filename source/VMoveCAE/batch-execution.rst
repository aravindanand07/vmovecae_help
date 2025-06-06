VMoveCAE Batch Translation
==========================
VCollab Suite provides a batch utility called VMoveCAEBatch.exe. It is
used to generate *Cax* files without user intervention and helps CAE
analysts in automating the *Cax* generation process. Its usage is as
follows:

**VMoveCAEBatch.exe [option=value] <model_file> [results_file]
<cax_file>**

The <model_file> and the <cax_file> are mandatory arguments to the
VMoveCAEBatch.exe. They represent the file paths of the input CAE model
file as well as the output *Cax* file.

One very common usage scenario of VMoveCAE is to translate all the
parts, and results from the given model file into a *Cax* file. This can
be achieved by providing the model file path and cax file path
specifying no options. For example, the following command loads the file
viewer_tutorial.odb from abaqus folder and creates a *Cax* file named
viewer_tutorial.cax under cax folder.

**VMoveCAEBatch.exe abaqus\viewer_tutorial.odb cax\viewer_tutorial.cax**

Many native CAE software split the simulation data into model and result
files. An example to this is, the Fluent .cas and .dat files. The .cas
file predominantly consists of the mesh, boundary conditions and initial
conditions where as the .dat file contains the simulation results. In
such cases, VMoveCAE supports appending results from a result file to
the mesh from the corresponding model file. The results file path is
provided by using the [results_file] optional argument. For successful
translation, the [results_file] and the <model_file> should correspond
to the same case. User also has to remember that this feature is
available only for certain file types. The following example describes
how to translate mesh and results stored in different files to *Cax*.

**VMoveCAEBatch.exe fluent/ic3d1000.cas fluent/ic3d1000.dat
cax/ic3d1000.cax**

VMoveCAEBatch translates all parts, results and instances when no
options are specified on the command line.
