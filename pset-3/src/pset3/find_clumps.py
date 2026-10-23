"""Rosalind BA1E: Find Patterns Forming Clumps in a String."""


def findClumps(genome: str, k: int, L: int, t: int) -> set[str]:
    """Return distinct k-mers appearing at least t times in any length-L window.

    Count overlapping occurrences fully contained within each window.
    Assume uppercase DNA, 1 <= k <= L <= len(genome), and t >= 1.
    Each qualifying k-mer appears only once in the returned set.
    """
    # TODO: Implement clump finding.
    n = len(genome)
    clumps: set[str] = set()
    counts: dict[str, int] = {}

    #count kmers in first window
    for i in range(L - k + 1):
        kmer = genome[i:i + k]
        counts[kmer] = counts.get(kmer, 0) + 1
    for kmer, c in counts.items():
        if c >= t:
            clumps.add(kmer)

    #slide window one pos at a time
    for start in range(1, n - L + 1):
        #remove kmer that left the window
        old = genome[start - 1:start - 1 + k]
        counts[old] -= 1
        if counts[old] == 0:
            del counts[old]

        #add kmer that entered the window
        new = genome[start + L - k:start + L]
        counts[new] = counts.get(new, 0) + 1
        if counts[new] >= t:
            clumps.add(new)

    return clumps