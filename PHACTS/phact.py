import os
import subprocess
from Bio.Data import CodonTable
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
import csv

# Path to the phacts.py tool
PHACTS_TOOL = "/home/karyna/.local/lib/python3.10/site-packages/PHACTS/phacts.py"

# Path to the folder containing the files to be tested
main_dir = '/home/karyna/Project_final/data/'
TEST_FOLDERS = ['GCA_028515195.1', 'GCA_027582695.1', 'GCA_028515145.1', 'GCA_014656645.1', 'GCA_002605545.1', 'GCA_028514995.1', 'GCA_004989725.1', 'GCA_028515085.1']
TEST_FOLDERS = ['GCA_028515195.1', 'GCA_027582695.1', 'GCA_028515145.1', 'GCA_002605545.1', 'GCA_028514995.1', 'GCA_004989725.1', 'GCA_028515085.1']

index=0


translation_table = CodonTable.unambiguous_dna_by_id[11]
for index in TEST_FOLDERS:
    full_path = main_dir+index
# Read the fasta files in the directory
    for file_name in os.listdir(full_path):
        file_path = os.path.join(full_path, file_name)
        if not file_name.endswith(".fna"):
            continue  # Skip non-fasta files

        # Generate the output file name
        output_file = os.path.splitext(file_name)[0] + "_translated.fasta"

        # Read the fasta file and extract the sequence
        record = SeqIO.read(file_path, "fasta")
        dna_sequence = Seq(str(record.seq))
        # Get the translation table for table 11
        translation_table = CodonTable.unambiguous_dna_by_id[11]

        # Translate the DNA sequence using table 11
        translated_sequence = dna_sequence.translate(table=translation_table)

        # Save the translated sequence in a separate output file
        output_path = os.path.join(full_path, output_file)
        SeqIO.write(SeqRecord(translated_sequence,
                                    id=record.id,
                                    description=record.description), output_path, "fasta")
        
        # Check if the file of translated sequence was created
        if os.path.isfile(output_path):
            print(output_path)
            # Run phacts.py on the file
            result=subprocess.run(["time", PHACTS_TOOL, output_path], capture_output=True, text=True)
            output_file = "/home/karyna/Project_final/PHACTS/phacts_output_"+index+".csv"
            output = result.stdout
            execution_time = result.stderr
            execution_time_seconds = float(execution_time.strip().split("user", 1)[0])
            execution_time_minutes = execution_time_seconds / 60

            with open(output_file, "w", newline="") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['fasta_name','Output', 'Nucleo_Seq_length','Execution Time'])
                writer.writerow([index, output, len(dna_sequence),execution_time_minutes])

