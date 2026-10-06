from frequent_words import PatternCount as inclass_pattern_count


def patternCount(text: str, pattern: str) -> int:
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i + len(pattern)] == pattern:
            count += 1  
    return count
