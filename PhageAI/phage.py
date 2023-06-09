import os
import csv
import pickle
import re
from phageai.lifecycle.classifier import LifeCycleClassifier

# pip install phageai
# change the access_token "lcc"
# change main_dir_path, start_subdirectory
# change csv_file and out_file names for each batch 


lcc = LifeCycleClassifier(access_token='wGaMa7QMgr8PSIhDbwDQEHAAcGkMVN')
main_dir_path = '/home/karyna/Project/data'
start_accession = 'GCA_000887755.1'
csv_file = "phageai_report2.csv"
out_file='pAI_2.pkl'


start_subdirectory=main_dir_path+start_accession
def SelectGenome(main_dir_path, start_subdirectory):
    subdirectories = sorted([os.path.join(main_dir_path, subdir) for subdir in os.listdir(main_dir_path) if os.path.isdir(os.path.join(main_dir_path, subdir))])
    start_index = subdirectories.index(start_subdirectory)
    if start_index <= (len(subdirectories)-1)-100:
        end_index = min(start_index + 100, len(subdirectories))
    else:
        end_index = len(subdirectories)-1
        print('no more genomes to run for next batch')
    return subdirectories, start_index, end_index, subdirectories[end_index]

def paths_aux(start_subdirectory):
    for subdir, dirs, files in os.walk(start_subdirectory):
        for single_fasta_file in files:
            # Check if the file is a FASTA file
            if single_fasta_file.endswith('.fna'):
                try:
                    # Generate the full path to the FASTA file
                    fasta_path = os.path.join(subdir, single_fasta_file)

                except Exception as e:
                    print(f'[PhageAI] Phage {single_fasta_file} raised an exception "{e}"')
    return fasta_path

def run(prediction_results = {}):
    limits = SelectGenome(main_dir_path, start_subdirectory)
    print("Next batch run have to start in: ", limits[3])
    for subdir_run in range(limits[1],limits[2]):
        # print(limits[0][subdir_run])
        fasta_path=paths_aux(limits[0][subdir_run])
        # Generate the prediction for the current FASTA file
        prediction_results[fasta_path] = lcc.predict(fasta_path=fasta_path)
    return prediction_results

with open(out_file, 'wb') as f:
    pAI=run()
    pickle.dump(pAI, f)

with open(out_file, 'rb') as f:
    pAI_result = pickle.load(f)

# Prepare CSV report as a final result
csv_columns = [
    'fasta_name', 'predicted_lifestyle', 'prediction_accuracy',
    'gc', 'sequence_length'
]

with open(csv_file, 'w') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=csv_columns)
    writer.writeheader()

    for fasta_name, phage_data in pAI_result.items():
        GCA_name = re.search(r'{}/(GCA_[^/]+)'.format(re.escape(str(main_dir_path))), fasta_name)

        if GCA_name:
            GCA_id = GCA_name.group(1)
            # print(GCA_id)
        data_to_write = {
            'fasta_name': GCA_id,
            'predicted_lifestyle': phage_data['predicted_lifecycle'],
            'prediction_accuracy': phage_data['prediction_accuracy'],
            'gc': phage_data['gc'],
            'sequence_length': phage_data['sequence_length']
        }
        writer.writerow(data_to_write)
    print('done')

