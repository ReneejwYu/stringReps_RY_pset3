def deBruijnFromKmers(patterns: list[str]) -> list[list[str]]:
    prefixes = {}

    for pattern in patterns:
        prefix = pattern[:-1]
        suffix = pattern[1:]

        if prefix not in prefixes:
            prefixes[prefix] = []
        prefixes[prefix].append(suffix)

    result = []

    for prefix in sorted(prefixes):
        result.append([prefix] + sorted(prefixes[prefix]))

    return result
