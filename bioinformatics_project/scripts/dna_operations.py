"""
This is a script that performs the following operations on DNA sequences:
    - Returns the complement
    - Returns the reverse 
    - Returns the reverse complement
"""

import sys
import argparse

# return the complement of a DNA sequence
def complement(sequence):
    # defining complementary base pairs
    complement_map = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    }
    
    return ''.join(complement_map[base] for base in sequence.upper())

#print(complement('CCTCAGC'))
#print(complement('cctagc'))

# return the reverse of a DNA sequence
def reverse(sequence):
    return sequence[::-1].upper()  

#print(reverse('CCTCAGC'))
#print(reverse('cctagc'))

# return the reverse complement of a DNA sequence
def reverse_complement(sequence):
    return reverse(complement(sequence))

#print(reverse_complement('CCTCAGC'))
#print(reverse_complement('cctagc'))

def main():
    # setting up command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('sequence', type=str, help="Input DNA sequence")

    args = parser.parse_args()
    input_seq = args.sequence.upper()

    # performing operations
    complement_seq = complement(input_seq)
    reverse_seq = reverse(input_seq)
    rev_comp_seq = reverse_complement(input_seq)

    # outputting results
    print(f"Original sequence: {input_seq}")
    print(f"Complement: {complement_seq}")
    print(f"Reverse: {reverse_seq}")
    print(f"Reverse complement: {rev_comp_seq}")

if __name__ == "__main__":
    main()


