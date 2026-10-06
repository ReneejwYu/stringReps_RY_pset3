def patternIndex(text: str, pattern: str) -> list[int]:
    indices = []
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i + len(pattern)] == pattern:
            indices.append(i)
    return indices