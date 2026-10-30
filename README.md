# CODON TABLE GENERATOR

## Python Assessment 2 – M.Sc. Bioinformatics

### 1. Project Overview

The Codon Table Generator is a Python-based program developed to translate DNA and RNA nucleotide sequences into their corresponding amino acids using the standard genetic code.

A codon consists of three nucleotides. Each codon specifies an amino acid or a stop signal during protein synthesis.

### 2. Objectives

* Create a dictionary containing all 64 possible codons.
* Accept DNA and RNA sequences from the user.
* Validate nucleotide sequences.
* Divide nucleotide sequences into groups of three.
* Translate codons into their corresponding amino acids.
* Identify start and stop codons.
* Handle incomplete codons.
* Display the complete codon table and translation results.

### 3. Tools and Technologies

* Programming Language: Python
* Code Editor: Visual Studio Code
* Version Control: Git
* Code Hosting Platform: GitHub

### 4. Methodology

The project follows these steps:

1. **Codon Table Creation:** A Python dictionary is created containing all 64 codons and their corresponding amino acids.
2. **Sequence Input:** The user enters a DNA or RNA nucleotide sequence.
3. **Input Validation:** The program checks whether the sequence contains valid nucleotide characters.
4. **RNA Conversion:** RNA sequences containing uracil (U) are converted into the corresponding DNA format by replacing U with T.
5. **Codon Identification:** The sequence is divided into groups of three nucleotides.
6. **Translation:** Each codon is matched with its corresponding amino acid using the dictionary.
7. **Start and Stop Identification:** ATG is identified as the start codon, while TAA, TAG and TGA are identified as stop codons.
8. **Incomplete Codon Handling:** Any remaining one or two nucleotides are displayed separately and are not translated.
9. **Output Display:** The complete codon table and translation results are displayed.

### 5. Sample Input

ATGGCTTTTTAA

### 6. Expected Output

* Codons: ATG – GCT – TTT – TAA
* Amino Acids: Methionine – Alanine – Phenylalanine – Stop
* Start Codon: ATG
* Stop Codon: TAA
* Incomplete Codon: None

### 7. GitHub Codon Table Comparison

The custom codon table developed in this project was compared with the standard genetic code implemented in the GitHub repository:

**Reference Repository:** linsalrob/genetic_codes

https://github.com/linsalrob/genetic_codes

The reference repository provides Python and C implementations for translating DNA sequences using NCBI genetic code tables.

**Comparison:**

| Parameter                 | Our Project                    | GitHub Reference    |
| ------------------------- | ------------------------------ | ------------------- |
| Standard genetic code     | Yes                            | Yes                 |
| Number of codons          | 64                             | 64 in standard code |
| Codon mapping             | Python dictionary              | Genetic code tables |
| DNA translation           | Yes                            | Yes                 |
| RNA translation           | Yes, through U-to-T conversion | Yes                 |
| Alternative genetic codes | No                             | Yes                 |

**Observation:**

Both implementations use the standard genetic code for the 64 codons. The codon-to-amino-acid assignments are expected to match when the standard genetic code (NCBI translation table 1) is selected.

Our project uses a simple dictionary-based approach, whereas the reference repository provides additional support for alternative genetic codes.

### 8. Applications

* Understanding the genetic code.
* Learning DNA and RNA translation.
* Basic bioinformatics sequence analysis.
* Understanding the relationship between nucleotide sequences and amino acids.
* Practising Python programming concepts.

### 9. Limitations

* The program uses only the standard genetic code.
* It does not identify complete open reading frames.
* It does not automatically find the correct reading frame.
* It translates codons in the given reading frame without stopping at the first stop codon.

### 10. Future Improvements

* Add support for alternative genetic codes.
* Identify open reading frames (ORFs).
* Allow translation in all six reading frames.
* Display amino acids using three-letter and one-letter abbreviations.
* Develop a graphical user interface.

### 11. Conclusion

The Codon Table Generator successfully demonstrates how Python dictionaries, loops, conditional statements and string manipulation can be applied to biological sequence analysis. It translates DNA and RNA sequences into their corresponding amino acids and identifies start and stop codons. This project provides a basic understanding of computational biology and the genetic code.

### 12. References

1. NCBI – The Genetic Codes: https://www.ncbi.nlm.nih.gov/datasets/docs/v2/data-processing/taxonomy-processing/genetic-codes/
2. GitHub – Genetic Codes by Robert A. Edwards: https://github.com/linsalrob/genetic_codes
