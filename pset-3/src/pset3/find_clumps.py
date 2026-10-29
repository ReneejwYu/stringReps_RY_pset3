"""Rosalind BA1E: Find Patterns Forming Clumps in a String."""

from frequency_array import PatternCount

def findClumps(genome: str, k: int, L: int, t: int) -> set[str]:
    """Return distinct k-mers appearing at least t times in any length-L window.

    Count overlapping occurrences fully contained within each window.
    Assume uppercase DNA, 1 <= k <= L <= len(genome), and t >= 1.
    Each qualifying k-mer appears only once in the returned set.
    """
    # TODO: Implement clump finding.
    clumps = set()

    for i in range(len(genome) - L + 1):
        window = genome[i:i+L]

        for j in range(len(window) - k + 1):
            pattern = window[j:j+k]

            if PatternCount(window, pattern) >= t:
                clumps.add(pattern)

    return clumps

print(" ".join(sorted(findClumps("CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGAAGAGAAGAGGAAACACGACACGACATTGCGACATAATGTACGAATGTAATGTGCCTATGGC", 5,  75, 4))))