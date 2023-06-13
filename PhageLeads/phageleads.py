import os

# # Path to the folder containing the files to be analyzed
# folder_path = r"C:\Users\Karyna\Desktop\Github\Project\data"

#install abricate

main_dir_path = '/home/karyna/Project/data'


# Loop through all files in the folder
for root, dirs, files in os.walk(main_dir_path):
    for file in files:
        # Get the full path of the file
        file_path = os.path.join(root, file)
        # # Run Abricate on the file with the specified database
        os.system(f"abricate --db vfdb")
        os.system(f"abricate {file_path}")

