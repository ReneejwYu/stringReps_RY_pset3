def deBruijnFromString(k: int, text: str) -> list[list[str]]:
    prefixes = {}

    for i in range(len(text) - k + 1):
        pattern = text[i:i+k]
        prefix = pattern[:-1]
        suffix = pattern[1:]

        if prefix not in prefixes:
            prefixes[prefix] = []
        prefixes[prefix].append(suffix)

    result = []

    for prefix in sorted(prefixes):
        result.append([prefix] + sorted(prefixes[prefix]))

    return result

