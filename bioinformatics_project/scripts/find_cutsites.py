"""
This is a script that finds pairs of restriction enzyme cut sites that are 80-120 kbp apart
in a given FASTA file. This is the workflow:
    1. Accept 2 arguments: FASTA file path and a cut site sequence
    2. Read in FASTA file, save the DNA sequence, and omit whitespaces
    3. Find all occurrences of specified cut site in the DNA sequence
    4. Find all pairs of cut site locations that are 80-120 kbp apart
    5. Print total number of cut site pairs found and positions of the first 5 pairs
    6. Saves a summary of results in the results directory as 'cutsite_summary.txt'
"""

import argparse

# read FASTA file and return whitespace-omitted DNA sequence
def read_fasta(file_path):
    with open(file_path, 'r') as fasta_file:
        dna_sequence = ''.join(line.strip() for line in fasta_file)
    return dna_sequence


# find all occurences of specified cut site in DNA sequence
def find_cut_sites(dna_sequence, cut_site):
    # removing and identifying | character from cut site
    cut_site_length = cut_site.replace('|', '')
    cut_position = cut_site.index('|')

    positions = []
    start = 0

    # search for cut site in sequence
    while True:
        start = dna_sequence.find(cut_site.replace('|', ''), start)
        
        if start == -1:
            break

        positions.append(start + cut_position)
        start += len(cut_site_length)

    return positions


# find all pairs of cut site locations that are 80-120 kbp apart
def find_pairs(positions):
    pairs = []
    n = len(positions)

    for i in range(n):
        for j in range(i + 1, n):
            distance = positions[j] - positions[i]
            if 80000 <= distance <= 120000:
                pairs.append((positions[i], positions[j]))

    return pairs


# save summary of results in results directory
def save_summary(cut_site, total_cut_sites, cut_site_pairs, output_file):
    with open(output_file, 'w') as f:
        f.write(f"Analyzing cut site: {cut_site}\n")
        f.write(f"Total cut sites found: {total_cut_sites}\n")
        f.write(f"Cut site pairs 80-120 kbp apart: {len(cut_site_pairs)}\n")
        f.write("First 5 pairs:\n")
        for i, (first, second) in enumerate(cut_site_pairs[:5]):
            f.write(f"{i + 1}. {first} - {second}\n")


def main():
    # setting up command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", type=str, help="FASTA file path")
    parser.add_argument("cut_site", type=str, help="Cut site sequence")
    
    # parsing arguments
    args = parser.parse_args()
    fasta_file = args.file_path
    cut_site_seq = args.cut_site

    # performing operations
    dna_seq = read_fasta(fasta_file)
    cut_site_pos = find_cut_sites(dna_seq, cut_site_seq)
    cut_site_pairs = find_pairs(cut_site_pos)

    # saving summary output to file path
    output_file = "bioinformatics_project/results/cutsite_summary.txt"
    
    save_summary(cut_site_seq, len(cut_site_pos), cut_site_pairs, output_file)

    # printing output 
    print(f"Analyzing cut site: {cut_site_seq}")
    print(f"Total cut sites found: {len(cut_site_pos)}")
    print(f"Cut site pairs 80-120 kbp apart: {len(cut_site_pairs)}")
    print("First 5 pairs:")
    for i, (first, second) in enumerate(cut_site_pairs[:5]):
        print(f"{i + 1}. {first} - {second}")

if __name__ == "__main__":
    main()