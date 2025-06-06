Format Overview
===============

-  The following screenshot provides an overview of the input file
   contents.

      .. figure:: _images/file-sections-data.png
         :alt: Input File format

         Input File format

-  Translation inputs are categorized into multiple sections.

-  Currently supported sections: Files, Parts, Results, Steps

-  Sections are made of data.

-  Each line can be a section, data, a continuation line or a comment.

-  Section lines start with ``*``, data lines start with ``-`` and
   continuation lines start with ``,``.

-  Everything else is considered as a comment and is ignored.

-  A section can’t appear more than once in an input file.

-  The following examples show various parts of a section/data line.

      .. figure:: _images/line-syntax.png
         :alt: Line Syntax

         Line Syntax

-  The following screenshot shows a few examples.

      .. figure:: _images/line-format.png
         :alt: Line format

         Line format

-  Sections and data lines need to specify the name.

-  Data lines for a some sections (STEP section) need the values to be
   specified along with the data name.

-  Both sections and data lines are made of attributes separated by
   ``,`` characters.

-  Attribute is of the form ``<attribute_name>=<attribute_value>``.

-  Attribute value is optional in many cases. If attribute value is not
   specified, the default value is used.

-  If user needs to specify a list of values for any key, the user needs
   to specify them in quotes and using ``,`` as separator.

-  All the keywords (name, value, attribute name and attribute value)
   are case insensitive, except for the file names.
