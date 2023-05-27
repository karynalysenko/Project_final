import os

# # Path to the folder containing the files to be analyzed
# folder_path = r"C:\Users\Karyna\Desktop\Github\Project\data\GCA_000887755.1\GCA_000887755.1_ViralProj60117_genomic.fna"
# folder_path = r"C:\Users\Karyna\Desktop\Github\Project\data"

#install anaconda
#install abricate
#install any2fasta

def SelectGenome(main_dir_path, start_subdirectory):
    subdirectories = sorted([os.path.join(main_dir_path, subdir) for subdir in os.listdir(main_dir_path) if os.path.isdir(os.path.join(main_dir_path, subdir))])
    start_index = subdirectories.index(start_subdirectory)
    end_index = min(start_index + 100, len(subdirectories))
    return subdirectories, start_index, end_index, subdirectories[end_index - 1]

main_dir_path = '/home/karyna/Project/data'
start_subdirectory = '/home/karyna/Project/data/GCA_000887755.1'

test=SelectGenome(main_dir_path, start_subdirectory)
# print(test[0][0],test[0][1],test[0][2])

# Loop through all files in the folder
for root, dirs, files in os.walk(main_dir_path):
    for file in files:
        # Get the full path of the file
        file_path = os.path.join(root, file)
        # # Run Abricate on the file with the specified database
        os.system(f"abricate --db vfdb")
        os.system(f"abricate {file_path}")

