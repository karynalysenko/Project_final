import os
import subprocess
# import phacts

# Path to the phacts.py tool
PHACTS_TOOL = "/home/karyna/.local/lib/python3.10/site-packages/PHACTS/phacts.py"

# Path to the folder containing the files to be tested
# TEST_FOLDER = r'C:\Users\Karyna\Desktop\Github\Project\data\GCA_000887755.1\'
TEST_FOLDER = '/home/karyna/Project/data/GCA_000887755.1/GCA_000887755.1_ViralProj60117_genomic.fna'

# # Loop through each file in the folder
for file_name in os.listdir(TEST_FOLDER):
    # file_path = os.path.join(TEST_FOLDER, file_name)
    print(file_name)

    # # Check if the file is a regular file
    # if os.path.isfile(file_path):
    #     # Run phacts.py on the file
    #     subprocess.run([PHACTS_TOOL, file_path])


###FAZER
##########3Com Bio.SeqIO, traduzir as seqs e ver os seus tamanhos