
from hamming_distance import hammingDistance

def approximatePatternMatching(pattern: str, text: str, d: int) -> list[int]:
    matched_position = []
    for i in range(len(text)-len(pattern)+1):
        if  hammingDistance(pattern, text[i:i+len(pattern)]) <= d:
            matched_position.append(i)
    return matched_position
