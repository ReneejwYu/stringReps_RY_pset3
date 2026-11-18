def stringComposition(k: int, text: str) -> list[str]:
    composition = []
    for i in range(len(text) - k + 1):
        composition.append(text[i:i + k])
    sorted_composition = sorted(composition)
    return sorted_composition
