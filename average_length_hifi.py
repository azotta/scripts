import gzip

def calculate_read_lengths(file_path):
    total_length = 0
    max_length = 0
    min_length = float('inf')
    read_count = 0

    with gzip.open(file_path, 'rt') as file:
        for line in file:
            if line.startswith('@'):  # Identifies the start of a read
                read_count += 1
                sequence = next(file).strip()
                length = len(sequence)
                total_length += length

                if length > max_length:
                    max_length = length

                if length < min_length:
                    min_length = length

    average_length = total_length / read_count

    return average_length, max_length, min_length

# Provide the path to your compressed FASTQ file
file_path = 'path/to/your/file.fastq.gz'

average_length, max_length, min_length = calculate_read_lengths(file_path)

print("Average length:", average_length)
print("Maximum length:", max_length)
print("Minimum length:", min_length)

