"""
This is a script to generate a random DNA sequence and saves it in FAST format.
"""

import random 
import textwrap
import os

# generate a random DNA sequence of 1 million base pairs (using A, C, G, T)
def generate_dna_seq(length):
    return ''.join(random.choices('ACGT', k=length))


# save the DNA sequence in FASTA format in the data directory
def save_to_fasta(sequence, file_path):
    # formatting the sequence with 80 base pairs per line
    formatted_sequence = '\n'.join(textwrap.wrap(sequence, width=80))

    # writing the FASTA formatted sequence to file
    with open(file_path, 'w') as fasta_file:
        fasta_file.write(formatted_sequence + '\n')


def main():
    # generating random DNA sequence of 1 mill BPS
    dna_sequence = generate_dna_seq(1000000)

    # defining output path
    output_dir = "bioinformatics_project/data"
    output_file = os.path.join(output_dir, "random_sequence.fasta")
    os.makedirs(output_dir, exist_ok=True)

    # saving to FASTA format
    save_to_fasta(dna_sequence, output_file)

    print(f"Random DNA sequence generated and saved to {output_file}")


if __name__ == "__main__":
    main()
