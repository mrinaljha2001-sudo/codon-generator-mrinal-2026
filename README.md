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
