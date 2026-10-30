# CODON TABLE GENERATOR

## Python Assessment 2 – M.Sc. Bioinformatics

1. Project Summary

The Codon Table Generator is a Python program that translates DNA and RNA nucleotide sequences into amino acids based on the standard genetic code.

A codon is made up of three nucleotides. It provides the code for an amino acid or a termination signal during the synthesis of a protein.

2. Objectives

Make a dictionary that contains 64 dictionaries for the codons.
User provides sequence for DNA and RNA.
Validate nucleotide sequences.
Divide nucleotide sequences into groups of three.
Translate codons into their corresponding amino acids.
Identify start and stop codons.
Handle incomplete codons.
Show codon table and translation.

3. Tools and Technologies

Programming Language: Python

Editor: Visual Studio Code

Version Control: Git

Platform to host your code: GitHub

4. Methodology

The project follows these steps:

Codon Table Python dict: All 64 codons with associated amino acids defined.
Sequence Input: User provides a nucleotide sequence of either DNA or RNA.
. Proof reading: The entire sequence is checked to ensure only acceptable nucleotide characters are present.
Within the RNA sequences T's in the corresponding DNA are represented by U.
Locating codons: Sequence of the two nucleotide bases is thus grouped into units of three.
Definition: Dictionary of matching each codon with its appropriate amino acid.
Begin and Stop sites ATG is designated as the start codon and TAA, TAG and TGA are designated as stop codons.
Partial Codons: if 1 or 2 base remaining at the end, it is shown at the bottom. Also not translated.
Output Display: Full coding table and translation outputs.

5. Sample Input

ATGGCTTTTTAA

6. Expected Output

Codons: ATG - GCT - TTT - TAA

Amino Acids: Methionine – Alanine – Phenylalanine – Stop

Start Codon: ATG

Termination (Stop Codon): TAA

Incomplete Codon: None

7. GitHub Codon Table Comparison

This custom codon table generated in this project was compared to the actual genetic code used in the Github repository:

Reference Repository: linsalrob/genetic_codes

https://github.com/linsalrob/genetic_codes

The reference repository contains the Python and C code to translate a DNA sequence in the NCBI genetic code tables.

Comparison:

Parameter Our Project GitHub Reference

Standard genetic code Yes

Number of codons 64 64 in traditional code
Codon mapping Python dictionary Genetic code tables

DNA translation Yes

RNA translation Yes, through U-to-T conversion Yes

Other genetic codes No Yes

Observation:

The code tables of both implementations are based on the standard genetic code for 64 codons. When the standard genetic code (NCBI translation table 1) is selected then the code table to amino acids must be the same.

Our implementation employs a straightforward dictionary algorithm, whereas the reference repository offers backup support for alternate codes.

8. Applications

Understanding the genetic code.
Learning DNA and RNA translation.
Basic bioinformatics sequence analysis.
Explain the correlation between amino acids and the sequence of nucleotides.
Practising Python programming concepts.

9. Limitations

This program uses only Standard Code.
It does not detect full open reading frames.
It does not automatically determine the right reading frame.
The translation is performed in the reading frame indicated, not stopping at the first implied stop codon.

10. Future Improvements

Add support for alternative genetic codes.
Identify open reading frames (ORFs).
Allow translation in all six reading frames.
Show amino acids with three- and one-letter code.
Develop a graphical user interface.

11. Conclusion

This project successfully exhibits the ability of dictionaries in Python and use of string manipulation, if-else and for loop. It takes a DNA or RNA sequence and generates a table of codons with the amino acid names, start and stop codons. It is basic introduction to computational biology and genetic code.

### 12. References

1. NCBI – The Genetic Codes: https://www.ncbi.nlm.nih.gov/datasets/docs/v2/data-processing/taxonomy-processing/genetic-codes/
2. GitHub – Genetic Codes by Robert A. Edwards: https://github.com/linsalrob/genetic_codes  
