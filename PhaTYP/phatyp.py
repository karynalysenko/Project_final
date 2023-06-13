import os
import re

# cd PhaBOX (be in directory of PhaBOX)
# conda activate phabox (activate phabox env)
# run this file: python /home/karyna/Project/PhaTYP/phatyp.py (depends on user directory)

main_dir_path = '/home/karyna/Project/data'
rootpth = '/home/karyna/Project/PhaTYP/phatyp_results/'
midfolder = '/midfolder'
# Path to the PhaTYP executable
PhaTYP_path = '/home/karyna/PhaBOX/PhaTYP_single.py'

# Loop through all files in the folder
for root, dirs, files in os.walk(main_dir_path):
    for file in files:
        # Get the full path of the file
        file_path = os.path.join(root, file)
        if file.endswith('.fna'):
            GCA_name = re.search(r'^(GCA_[^_/]+)', file)
            if GCA_name:
                GCA_id = GCA_name.group(1)
                print(file_path)
                os.system(f"python {PhaTYP_path} --contigs {file_path} --rootpth {rootpth+GCA_id}")
