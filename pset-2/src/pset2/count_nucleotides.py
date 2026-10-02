def countNucleotides(text: str) -> dict[str, int]:
    # TODO: Write your code here.
    A_count = text.count('A')
    T_count = text.count('T')
    C_count = text.count('C')
    G_count = text.count('G')

    return {
        'A': A_count,
        'T': T_count,
        'C': C_count,
        'G': G_count
    }
    raise NotImplementedError("Implement countNucleotides")
