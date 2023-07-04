from Bio import SeqIO

# Path to the input FASTQ file
input_file = "all_MiMA.fastq"

# Path to the output FASTQ file for the selected reads
output_file = "min_50_mima.fastq"

# Minimum length threshold (50kb in this case)
min_length = 50000

# Open the output file for writing
with open(output_file, "w") as output_handle:
    # Iterate over each read in the input FASTQ file
    for record in SeqIO.parse(input_file, "fastq"):
        # Check if the length of the current read is greater than the threshold
        if len(record.seq) > min_length:
            # Write the selected read to the output file
            SeqIO.write(record, output_handle, "fastq")

