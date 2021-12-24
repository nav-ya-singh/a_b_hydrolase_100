# a_b_hydrolase_100

This script executes the following pipeline:

1. Pass in a pdb id txt file (throught the bash command line), download all the cif files from their pdb ids
> Run parse_download.py in its own directory. I suggest creating a folder/directory to separately store the parse_download.py, data_visulaization.py, text file, and cif.gz files.

_ON TERMINAL/COMMAND LINE:_
-> python parse_download.py a_b_hydrolase_100.txt

2. Count the number of amino acids in unique chains per cif file, and output plots of the amino acid counts and percentages for all the pdbs in the text file.
> During this step (data_visualization.py) on the command line, you must pass the name of the directory/folder (that stores all the cif.gz files) as an argument.

_ON TERMINAL/COMMAND LINE:_
-> python data_visualization.py ./

