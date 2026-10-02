"""Find the most frequent words of a given length in text."""

from .pattern_count import PatternCount


def FrequentWords(text: str, k: int) -> set[str]:
    """Return all length-k substrings with the highest occurrence count.

    Count overlapping, case-sensitive matches and include every tie once.
    Assume k is a positive integer. Return an empty set if k exceeds the
    length of text or text is empty.

    Example:
        FrequentWords("ATAT", 2) returns {"AT"}.
        FrequentWords("ATGC", 2) returns {"AT", "TG", "GC"}.

    PatternCount is already imported above. You can call
    PatternCount(text, pattern) directly in your implementation.
    """
    FrequentPatterns = set()
    count = []
    for i in range (len(text) - k +1):
        pattern = text[i:i+k]
        count.append (PatternCount(text,pattern))

    max_count = max(count)

    for i in range (len(text) - k +1):
        if count[i] == max_count:
            FrequentPatterns.add(text[i:i+k])
    return FrequentPatterns
    # TODO: Implement this function.
    raise NotImplementedError("Implement FrequentWords")