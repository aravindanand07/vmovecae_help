CaxInfo
=======
CaxInfo is a conole application to extract metadata from Cax files. This
metadata information includes the change history of the cax file, the
parts and element set information as well as the available results in
the Cax file. The metadata is printed on to the console by default. Its
usage is as follows.

*CaxInfo <cax_file> [output_file]*

Examples:

CaxInfo "bracket.cax"

The above example extracts the metadata from a cax file. This
information is formatted to XML format and printed to the console. The
metadata can also be directed into a file instead of printing into
screen by providing an output file on the command line as shown in the
following example.

CaxInfo "bracket.cax" "bracket-metadata.xml"

