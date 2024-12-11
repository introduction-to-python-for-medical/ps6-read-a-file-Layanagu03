def create_codon_dict(file_path):\
     path="data/codons.txt"
     file = open(file_path)
    rows = file.readlines()
    file.close()
    
    # Create an empty dictionary to store the codon-amino-acid pairs
    codon_dict = {}
    
    # Loop through each row to extract the codon and amino acid abbreviation
    for row in rows:
        row = row.strip().split('\t')  # Clean and split the row into parts
        if len(row) >= 3:  # Make sure there are at least 3 parts in the row
            codon = row[0]  # Get the codon (first cell)
            amino_acid_abbr = row[2]  # Get the amino acid abbreviation (third cell)
            codon_dict[codon] = amino_acid_abbr  # Update the dictionary
    
    return codon_dict


