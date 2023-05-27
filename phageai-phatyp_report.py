import pandas as pd
import os
# import csv
import re


#PhageAI#########################################
report1 = pd.read_csv("/home/karyna/Project/PhageAI/phageai_report1.csv").add_prefix('phageai_')
report2 = pd.read_csv("/home/karyna/Project/PhageAI/phageai_report2.csv").add_prefix('phageai_')

phageai_complete = pd.concat([report1,report2], axis = 0)
print(phageai_complete.head())
# print(phageai_complete.shape)

#PhaTYP#########################################

directory = "/home/karyna/Project/PhaTYP/phatyp_results"

def paths_aux(directory, csv_paths={}):
   for subdir, dirs, files in os.walk(directory):
       for csv_file in files:
           if csv_file.endswith('phatyp_prediction.csv'):
                csv_path = os.path.join(subdir, csv_file)
                csv_paths[csv_path] = csv_path
   return csv_paths

phatyp_complete = pd.DataFrame(columns=['fasta_name'])
for path in paths_aux(directory).values():
    report = pd.read_csv(path).add_prefix('phatyp_')
    GCA_name = re.search(r'{}/(GCA_[^/]+)'.format(re.escape(str(directory))), path)
    if GCA_name:
        GCA_id = GCA_name.group(1)
        report['fasta_name'] = GCA_id
        phatyp_complete = pd.concat([phatyp_complete, report], ignore_index=True)
print(phatyp_complete.head())


#JOIN OF PHAGEAI AND PHATYP##################################
# joined_df = pd.merge(phageai_complete, phatyp_complete, left_on='phageai_fasta_name', right_on='fasta_name', how='inner')
# print(joined_df)

# joined_df.to_csv('phatyp_phageai_report.csv', index=False)

for gca_id in phageai_complete['phageai_fasta_name']:
    phageai_virulent_count=phageai_complete.loc[phageai_complete['phageai_predicted_lifestyle'] == 'Virulent']
    phageai_temperate_count=phageai_complete.loc[phageai_complete['phageai_predicted_lifestyle'] == 'Temperate']


for gca_id in phatyp_complete['fasta_name']:
    phatyp_virulent_count=phatyp_complete.loc[phatyp_complete['phatyp_Pred'] == 'virulent']
    phatyp_temperate_count=phatyp_complete.loc[phatyp_complete['phatyp_Pred'] == 'temperate']

#score mean
temperate_scores_phageai = phageai_complete.loc[phageai_complete['phageai_predicted_lifestyle'] == 'Temperate', 'phageai_prediction_accuracy'].mean()
temperate_scores_phatyp = phatyp_complete.loc[phatyp_complete['phatyp_Pred'] == 'temperate', 'phatyp_Score'].mean()

print(f"PhageAI: virulent count is {len(phageai_virulent_count)} temperate count is {len(phageai_temperate_count)}" )
print(f"PhaTYP: virulent count is {len(phatyp_virulent_count)} temperate count is {len(phatyp_temperate_count)}" )

print("Mean score for temperate rows in PhageAI:", temperate_scores_phageai)
print("Mean score for temperate rows in PhaTYP:", temperate_scores_phatyp*100)
print(phageai_temperate_count)