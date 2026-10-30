
# PROJECT: CODON TABLE GENERATOR
# Python Assessment 2

# 1. Create a dictionary containing all 64 codons

codon_table = {
    "TTT": "Phenylalanine", "TTC": "Phenylalanine",
    "TTA": "Leucine", "TTG": "Leucine",
    "TCT": "Serine", "TCC": "Serine",
    "TCA": "Serine", "TCG": "Serine",
    "TAT": "Tyrosine", "TAC": "Tyrosine",
    "TAA": "Stop", "TAG": "Stop",
    "TGT": "Cysteine", "TGC": "Cysteine",
    "TGA": "Stop", "TGG": "Tryptophan",

    "CTT": "Leucine", "CTC": "Leucine",
    "CTA": "Leucine", "CTG": "Leucine",
    "CCT": "Proline", "CCC": "Proline",
    "CCA": "Proline", "CCG": "Proline",
    "CAT": "Histidine", "CAC": "Histidine",
    "CAA": "Glutamine", "CAG": "Glutamine",
    "CGT": "Arginine", "CGC": "Arginine",
    "CGA": "Arginine", "CGG": "Arginine",

    "ATT": "Isoleucine", "ATC": "Isoleucine",
    "ATA": "Isoleucine", "ATG": "Methionine",
    "ACT": "Threonine", "ACC": "Threonine",
    "ACA": "Threonine", "ACG": "Threonine",
    "AAT": "Asparagine", "AAC": "Asparagine",
    "AAA": "Lysine", "AAG": "Lysine",
    "AGT": "Serine", "AGC": "Serine",
    "AGA": "Arginine", "AGG": "Arginine",

    "GTT": "Valine", "GTC": "Valine",
    "GTA": "Valine", "GTG": "Valine",
    "GCT": "Alanine", "GCC": "Alanine",
    "GCA": "Alanine", "GCG": "Alanine",
    "GAT": "Aspartic acid", "GAC": "Aspartic acid",
    "GAA": "Glutamic acid", "GAG": "Glutamic acid",
    "GGT": "Glycine", "GGC": "Glycine",
    "GGA": "Glycine", "GGG": "Glycine"
}

# 2. Define start and stop codons

start_codons = ["ATG"]

stop_codons = ["TAA", "TAG", "TGA"]

# 3. Display the complete codon table

def display_codon_table():

    print("\n========== COMPLETE CODON TABLE ==========")

    for codon, amino_acid in codon_table.items():
        print(codon, ":", amino_acid)

    print("Total codons:", len(codon_table))

# 4. Accept and validate the sequence

def validate_sequence(sequence):

    sequence = "".join(sequence.upper().split())

    if not sequence:
        print("Error: Sequence cannot be empty.")
        return None

    if "U" in sequence and "T" in sequence:
        print("Error: Do not mix DNA and RNA nucleotides.")
        return None

    if not all(base in "ATGC" for base in sequence):
        if not all(base in "AUGC" for base in sequence):
            print("Error: Enter only A, T, G, C or RNA bases A, U, G, C.")
            return None

    # Convert RNA into DNA format for translation
    sequence = sequence.replace("U", "T")

    return sequence

# 5. Divide sequence into codons

def divide_into_codons(sequence):

    codons = []

    for i in range(0, len(sequence) - 2, 3):
        codons.append(sequence[i:i+3])

    incomplete = sequence[len(codons) * 3:]

    return codons, incomplete

# 6. Translate codons into amino acids

def translate_sequence(codons):

    amino_acids = []

    for codon in codons:

        amino_acid = codon_table[codon]

        amino_acids.append(amino_acid)

    return amino_acids

# 7. Identify start and stop codons

def identify_start_stop(codons):

    starts = []
    stops = []

    for i, codon in enumerate(codons):

        if codon in start_codons:
            starts.append(codon)

        if codon in stop_codons:
            stops.append(codon)

    return starts, stops

# 8. Main program

def main():

    print("===================================")
    print("       CODON TABLE GENERATOR")
    print("===================================")

    sequence = input("\nEnter your DNA or RNA sequence: ")

    sequence = validate_sequence(sequence)

    if sequence is None:
        return

    # Display codon table
    display_codon_table()

    # Divide sequence into codons
    codons, incomplete = divide_into_codons(sequence)

    # Translate sequence
    amino_acids = translate_sequence(codons)

    # Identify start and stop codons
    starts, stops = identify_start_stop(codons)

    # Display results
    print("\n========== TRANSLATION RESULTS ==========")

    print("\nOriginal sequence:", sequence)

    print("\nCodons:", " - ".join(codons))

    print("\nAmino acids:", " - ".join(amino_acids))

    print("\nStart codons:", starts if starts else "None found")

    print("Stop codons:", stops if stops else "None found")

    if incomplete:
        print("\nIncomplete codon:", incomplete)
        print("Warning: Incomplete codon was not translated.")

    else:
        print("\nIncomplete codon: None")

    print("\n===================================")
    print("          PROGRAM COMPLETED")
    print("===================================")

# 9. Run the program

if __name__ == "__main__":
    main()