def to_rna(dna_strand):
    arn = ""
    for cadena in dna_strand:
        if cadena == "G":
            arn += "C"
        if cadena == "C":
            arn += "G"
        if cadena == "T":
            arn += "A"
        if cadena == "A":
            arn += "U"
    return arn
