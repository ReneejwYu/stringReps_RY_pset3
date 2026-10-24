"""Rosalind BA1C: Find the Reverse Complement of a String."""

def reverseComplement(text: str) -> str:
    """Return the reverse complement of an uppercase DNA string.

    A pairs with T, and C pairs with G. Return the complementary
    nucleotides in reverse order.
    """
    complement = {"A": "T", "T": "A", "C": "G", "G": "C"}
    reverse_comp = ""

    for base in text[::-1]:
        reverse_comp += complement[base]

    return reverse_comp

