Support for Compressed Files and Archives
==========================================

Users can select and load an archive or compressed file in VMoveCAE GUI. They can also pass an archive or compressed file path in lieu of the model file during batch execution. The following archives and compressed file formats are supported. 

  - ZIP (\*.zip) archive files 
  - Tar (\*.tar) archive files 
  - GZip (\*.gz) compressed files 
  - BZip2 (\*.bz2) compressed files

VMoveCAE extracts the archives and the compressed files into a temporary folder. It then tries to locate a file of a supported format from this temporary folder to load and translate. If VMoveCAE fails to locate files of any supported format, it will show an error to the user. If the folder contains more than one file of supported formats, it may load any file and display it to the user. These uncompressed files are deleted automatically during VMoveCAE's execution. 

**FEMZIP compressed d3plot files**


VMoveCAE can run FEMUNZIP executable, extract the uncompressed files and load them for translation. The procedure to enable this is provided below. 

  - Specify the FEMUNZIP executable path by setting the VMOVECAE_FEMUNZIP_DYNA_PATH environment variable. For example,on a desktop running a Microsoft Windows operating system, the command to be entered is: 

    set **VMOVECAE_FEMUNZIP_DYNA_PATH=F:\Software\femzip\femunzip_dyna.exe**

  - Create and set the environment variable VMOVECAE_USE_FEMUNZIP to 1 to enable the FEMUNZIP execution.  

  - VMoveCAE recognizes files with extension ".fz" or those starting with "Zd3plot" as FEMZIP compressed d3plot files.
