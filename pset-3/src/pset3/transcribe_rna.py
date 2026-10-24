"""Rosalind RNA: Transcribing DNA into RNA."""
# import regex library
import re

def transcribeRNA(text: str) -> str:
    """Return the RNA string corresponding to an uppercase DNA coding strand.

    Replace each T with U, retaining the order of the other nucleotides.
    """
    rna = ""
    for base in text:
        if base == "T":
            rna += "U"
        else:
            rna += base
    return rna
