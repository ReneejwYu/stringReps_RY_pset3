def overlapGraph(patterns: list[str]) -> list[list[str]]:
    prefixes = {}
    graph = []

    for pattern in patterns:
        prefix = pattern[:-1]

        if prefix not in prefixes:
            prefixes[prefix] = []

        prefixes[prefix].append(pattern)

    for pattern in patterns:
        suffix = pattern[1:]

        if suffix in prefixes:
            for matching_pattern in prefixes[suffix]:
                graph.append([pattern, matching_pattern])

    return sorted(graph)