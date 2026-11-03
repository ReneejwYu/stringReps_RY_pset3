from frequent_words_with_mismatches import Neighbors 

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

def frequentWordsWithMismatchesAndReverseComplements(text: str, k: int, d: int) -> set[str]:

    frequency = {}

    #count approx match of patter
    for i in range(len(text) - k + 1):
        pattern = text[i:i+k]

        for neighbor in Neighbors(pattern, d):
            if neighbor not in frequency:
                frequency[neighbor] = 1
            else:
                frequency[neighbor] += 1

    #count the total of pattern and reverse pattern
    combined_frequency = {}

    for pattern in frequency:
        reverse = reverseComplement(pattern)
        combined_frequency[pattern] = (frequency.get(pattern, 0) + frequency.get(reverse, 0))
        combined_frequency[reverse] = combined_frequency[pattern]

    #find maximum frequency
    max_count = max(combined_frequency.values())

    frequent_patterns = set()

    for pattern, count in combined_frequency.items():
        if count == max_count:
            frequent_patterns.add(pattern)

    return frequent_patterns

result = frequentWordsWithMismatchesAndReverseComplements("ATAATGACATAATGACTTCTCGTATCGCATTTGATAATGACTCGCATTTGTGTATTCATTCTCGTATTCTCGTATCGCATTTGTCTGCTGGAATCGCATTTGTGTATTCAATAATGACTCTGCTGGAATGTATTCATGTATTCATCTGCTGGAATCGCATTTGTCTGCTGGAATCGCATTTGTGTATTCATCTGCTGGAATTCTCGTAATAATGACATAATGACTCGCATTTGATAATGACTCGCATTTGTTCTCGTATCGCATTTGATAATGACATAATGACTCGCATTTGTCTGCTGGAATTCTCGTAATAATGACTGTATTCATCTGCTGGAAATAATGACTTCTCGTAATAATGACTGTATTCATTCTCGTATTCTCGTAATAATGACTGTATTCAATAATGACATAATGACTCGCATTTGATAATGACATAATGACTCGCATTTGTTCTCGTATTCTCGTATGTATTCATCGCATTTGTCTGCTGGAATCTGCTGGAATCGCATTTGATAATGACATAATGACTTCTCGTAATAATGACTGTATTCATCTGCTGGAATCGCATTTGTGTATTCATGTATTCATCGCATTTGTCGCATTTGATAATGACTGTATTCATCGCATTTGTCTGCTGGAAATAATGACTCTGCTGGAATGTATTCATCGCATTTGTTCTCGTATTCTCGTATCTGCTGGAATGTATTCATTCTCGTATTCTCGTAATAATGACTTCTCGTATTCTCGTATCGCATTTGATAATGACTCTGCTGGAATGTATTCATTCTCGTAATAATGACTTCTCGTAATAATGACTCTGCTGGAAATAATGACTCTGCTGGAATCTGCTGGAATTCTCGTATGTATTCATGTATTCATCTGCTGGAATCGCATTTGTTCTCGTATTCTCGTATTCTCGTA",6,2)
print(result)