# a_b_hydrolase_100

This script executes the following pipeline:

1. Pass in a pdb id txt file (throught the bash command line), download all the cif files from their pdb ids
> Run parse_download.py in its own directory. I suggest creating a folder/directory to separately store just the pdb ids.

2. Count the number of amino acids in unique chains per cif file, and output plots of the amino acid counts and percentages for all the pdbs in the text file.
> During this step (data_visualization.py) on the bash command line, you must plug in the name of the directory that you created to store all the cif.gz files as an argument
