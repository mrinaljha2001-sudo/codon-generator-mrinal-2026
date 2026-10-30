CODON TABLE GENERATOR
Python Assessment 2 – M.Sc. Bioinformatics
1. Project Overview

The Codon Table Generator is a Python-based program developed to translate DNA and RNA nucleotide sequences into their corresponding amino acids using the standard genetic code.

A codon consists of three nucleotides. Each codon specifies an amino acid or a stop signal during protein synthesis.

2. Objectives
Create a dictionary containing all 64 possible codons.
Accept DNA and RNA sequences from the user.
Validate nucleotide sequences.
Divide nucleotide sequences into groups of three.
Translate codons into their corresponding amino acids.
Identify start and stop codons.
Handle incomplete codons.
Display the complete codon table and translation results.

3. Tools and Technologies
Programming Language: Python
Code Editor: Visual Studio Code
Version Control: Git
Code Hosting Platform: GitHub
4. Methodology

The project follows these steps:

Codon Table Creation: A Python dictionary is created containing all 64 codons and their corresponding amino acids.
Sequence Input: The user enters a DNA or RNA nucleotide sequence.
Input Validation: The program checks whether the sequence contains valid nucleotide characters.
RNA Conversion: RNA sequences containing uracil (U) are converted into the corresponding DNA format by replacing U with T.
Codon Identification: The sequence is divided into groups of three nucleotides.
Translation: Each codon is matched with its corresponding amino acid using the dictionary.
Start and Stop Identification: ATG is identified as the start codon, while TAA, TAG and TGA are identified as stop codons.
Incomplete Codon Handling: Any remaining one or two nucleotides are displayed separately and are not translated.
Output Display: The complete codon table and translation results are displayed.

5. Sample Input

ATGGCTTTTTAA
6. Expected Output
Codons: ATG – GCT – TTT – TAA
Amino Acids: Methionine – Alanine – Phenylalanine – Stop
Start Codon: ATG
Stop Codon: TAA
Incomplete Codon: None
7. GitHub Codon Table Comparison

The custom codon table developed in this project was compared with the standard genetic code implemented in the GitHub repository:

Reference Repository: linsalrob/genetic_codes

https://github.com/linsalrob/genetic_codes

The reference repository provides Python and C implementations for translating DNA sequences using NCBI genetic code tables.

Comparison:

Parameter	Our Project	GitHub Reference
Standard genetic code	Yes	Yes
Number of codons	64	64 in standard code
Codon mapping	Python dictionary	Genetic code tables
DNA translation	Yes	Yes
RNA translation	Yes, through U-to-T conversion	Yes
Alternative genetic codes	No	Yes

Observation:

Both implementations use the standard genetic code for the 64 codons. The codon-to-amino-acid assignments are expected to match when the standard genetic code (NCBI translation table 1) is selected.

Our project uses a simple dictionary-based approach, whereas the reference repository provides additional support for alternative genetic codes.
