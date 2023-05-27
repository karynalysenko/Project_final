import os
import pandas as pd
# import csv
import re

directory = "/home/karyna/Project/PhaTYP/phatyp_results"
csv_file_name = "phatyp_alltogether.csv"

def paths_aux(directory, csv_paths={}):
   for subdir, dirs, files in os.walk(directory):
       for csv_file in files:
           if csv_file.endswith('phatyp_prediction.csv'):
                csv_path = os.path.join(subdir, csv_file)
                csv_paths[csv_path] = csv_path
   return csv_paths

phatyp_complete = pd.DataFrame(columns=['fasta_name'])

for path in paths_aux(directory).values():
    report = pd.read_csv(path)
    GCA_name = re.search(r'{}/(GCA_[^/]+)'.format(re.escape(str(directory))), path)
    if GCA_name:
        GCA_id = GCA_name.group(1)
        # phatyp_complete = pd.concat([phatyp_complete, df_temp], ignore_index=True)
        report['fasta_name'] = GCA_id
    print(report)
