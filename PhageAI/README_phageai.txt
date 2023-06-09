Usage of PhageAI

This script is prepared to run batches of maximum 100 genomes per day. In case you have more than that, you'll receive an output in terminal of what would be the next folder to be run in the next day, so the 101st genome. 

After installation of the tool, to use it in a local machine, steps must be taken:
 -> change variable lcc - it's an access token associated to each user of Web PhageAI. This token can be found in the oficial Webpage
 -> change variable main_dir_path - this should be the path of the data files (genomes)
 -> change variable accessionId_test - list of accession numbers of genomes that user wants to test
 -> change variable start_accession - path of the starting folder path
 -> change variable csv_file - this is the name of the .csv output of the run (per batch of <100 genomes)
 -> change variable out_file - intermediate .pkl file that saves the run results


After each batch of run, a .pkl and .csv file will be created in the same folder of the script. 
