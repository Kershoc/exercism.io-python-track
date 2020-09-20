DNA2RNA = {
    "G":"C",
    "C":"G",
    "T":"A",
    "A":"U"
}

def to_rna(dna_strand):
    return "".join([DNA2RNA[ch] for ch in dna_strand])
