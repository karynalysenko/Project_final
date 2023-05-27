import os
import csv
import pickle
from pathlib import Path
from phageai.lifecycle.classifier import LifeCycleClassifier

lcc = LifeCycleClassifier(access_token='wGaMa7QMgr8PSIhDbwDQEHAAcGkMVN')

#main_dir_path = Path(r'C:\Users\Karyna\Desktop\Github\Project\data')
file_dir_path = Path(r'/home/karyna/Project/data/GCA_000887755.1/GCA_000887755.1_ViralProj60117_genomic.fna')
main_dir_path = '/home/karyna/Project/data'


# result = lcc.predict(fasta_path = r'C:\Users\Karyna\Desktop\Github\Project\data\GCA_000887755.1\GCA_000887755.1_ViralProj60117_genomic.fna')
# result = lcc.predict(fasta_path = main_dir_path)

#print(result)

###############################################
#def PhageAIrun(prediction_results = {}):
#    for subdir, dirs, files in os.walk(main_dir_path):
#        for single_fasta_file in files:
#            # Check if the file is a FASTA file
#            if single_fasta_file.endswith('.fna'):
#                try:
#                    # Generate the full path to the FASTA file
#                    fasta_path = os.path.join(subdir, single_fasta_file)

#                    # Generate the prediction for the current FASTA file
#                    prediction_results[fasta_path] = lcc.predict(fasta_path=fasta_path)

#                except Exception as e:
#                    print(f'[PhageAI] Phage {single_fasta_file} raised an exception "{e}"')
#    return prediction_results
#pAI=PhageAIrun()
###############################################

# with open('result.pkl', 'wb') as f:
#     pickle.dump(result, f)

# with open('result.pkl', 'rb') as f:
#     pAI = pickle.load(f)

# ## Python dict with prediction results
# for fasta, phageai in pAI.items():
#     print(fasta, phageai)

# # Prepare CSV report as a final result
# csv_columns = [
#     'fasta_name', 'predicted_lifestyle', 'prediction_accuracy',
#     'gc', 'sequence_length'
# ]

# # CSV file name
# csv_file = "phageai_report.csv"

# with open(csv_file, 'w') as csv_file:
#     writer = csv.DictWriter(csv_file, fieldnames=csv_columns)
#     writer.writeheader()

#     for fasta_name, phage_data in pAI.items():
#         print(fasta_name, 'aqui')
#         data_to_write = {
#             'fasta_name': 'name',
#             'predicted_lifestyle': pAI['predicted_lifecycle'],
#             'prediction_accuracy': pAI['prediction_accuracy'],
#             'gc': pAI['gc'],
#             'sequence_length': pAI['sequence_length']
#         }
#         writer.writerow(data_to_write)

#colect 100 genomes at the time
# start_dir_path = Path(r'/home/karyna/Project/data/GCA_000887755.1')
# start_dir_path = '/home/karyna/Project/data/GCA_015245225.1'
start_dir_path = '/home/karyna/Project/data/GCA_000887755.1'

def SelectGenome(main_dir_path, start_subdirectory):
    subdirectories = sorted([os.path.join(main_dir_path, subdir) for subdir in os.listdir(main_dir_path) if os.path.isdir(os.path.join(main_dir_path, subdir))])
    start_index = subdirectories.index(start_subdirectory)
    if start_index <= (len(subdirectories)-1)-100:
        end_index = min(start_index + 100, len(subdirectories))
    else:
        end_index = len(subdirectories)-1
        print('no more genomes to run for next batch')
    return subdirectories, start_index, end_index, subdirectories[end_index]

limits = SelectGenome(main_dir_path, start_dir_path) #tuplo index_0:all subdirs paths, index_1:start_index, index_2:end_index, index_3:subdir path of end_index
print(limits[3])

# print(limits[0][99])
# print(limits[1])
# for subdir_run in range(limits[1],limits[2]):
#     print(limits[0][subdir_run])
    
# print(SelectGenome(main_dir_path,start_dir_path))


# /home/karyna/Project/data/GCA_015245225.1
csv_columns = ['fasta_name']
import re
with open('all_genomes.csv', 'w') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=csv_columns)
    writer.writeheader()

    for root, dirs, files in os.walk(main_dir_path):
        for file in files:
            # Get the full path of the file
            file_path = os.path.join(root, file)
            # print(file)
            print(file_path)
            GCA_name = re.search(r'{}/(GCA_[^/]+)'.format(re.escape(str(main_dir_path))), file_path)
            # print(file)
            if GCA_name:
                GCA_id = GCA_name.group(1)
                print(GCA_id)
                data_to_write = {
                    'fasta_name': GCA_id}
                writer.writerow(data_to_write)
    print('done')