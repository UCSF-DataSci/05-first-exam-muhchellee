#!/bin/bash

# create main directory
mkdir -p bioinformatics_project

# create subdirectories
mkdir -p bioinformatics_project/data
mkdir -p bioinformatics_project/scripts
mkdir -p bioinformatics_project/results

# create empty Python files
touch bioinformatics_project/scripts/generate_fasta.py
touch bioinformatics_project/scripts/dna_operations.py
touch bioinformatics_project/scripts/find_cutsites.py

touch bioinformatics_project/results/cutsite_summary.txt

touch bioinformatics_project/data/random_sequence.fasta

# create README
echo "# Bioinformatics Project" > bioinformatics_project/README.md
echo "Project structure:" >> bioinformatics_project/README.md
echo "- **data**: contains FASTA data" >> bioinformatics_project/README.md
echo "- **scripts**: contains Python scripts" >> bioinformatics_project/README.md
echo "- **results**: contains output data" >> bioinformatics_project/README.md

# print output
echo "Project directory structure created successfully:"
tree bioinformatics_project