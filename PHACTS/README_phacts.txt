Usage of PHACTS

After installation of the tool, to use in a local machine, steps must be taken:
 -> change variable PHACTS_TOOL - path of the executable of PATH tool
 -> change variable main_dir - this should be the path of the data files (genomes)
 -> change variable accessionId_test - list of accession numbers of genomes that user wants to test
 -> change variable output - this is the path of the .csv output of the run (per genome)

This script will automatically run through the list accessionId_test, that should contain the acession numbers of the complete genomes. Each genome will be translated, using the translation table 11, and saved in the correspondent folder as .fasta. Then, PHACTS will run the new generated translated sequence and the result will be saved in a new .csv file named as "phacts_output_accessionID".


