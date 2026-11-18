def stringSpelledByGenomePath(patterns: list[str]) -> str:
    """Return the string spelled by the ordered genome path (BA3B)."""
    genome = patterns[0]
    for pattern in patterns[1:]:
        genome += pattern[-1]
    return genome