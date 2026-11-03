from hamming_distance import hammingDistance

#creating the neighbors of each k-mers in the text(genome)
def Neighbors(pattern: str, d: int) -> set[str]:
    neighbors = {""}

#starting from first letter in the patter
    for i in range(len(pattern)):
        new_neighbors = set()
        
        #list all the possible combination nucleotides for first two letters in the patterns
        for neighbor in neighbors:
            for nucleotide in "ACGT":
                new_pattern = neighbor + nucleotide

                #see whether they satisfied hamming distance requirement
                if hammingDistance(pattern[:i+1], new_pattern) <= d:
                    new_neighbors.add(new_pattern)

        neighbors = new_neighbors

    return neighbors

def frequentWordsWithMismatches(text: str, k: int, d: int) -> set[str]:
    frequency = {}

    for i in range(len(text) - k + 1):
        pattern = text[i:i+k]

        #generate all neighbors for each k-mer and put them in to a dictionary (patter,frequency)
        for neighbor in Neighbors(pattern, d):
            if neighbor not in frequency:
                frequency[neighbor] = 1

            frequency[neighbor] += 1

    #find the maximum frequency
    max_count = max(frequency.values())

    #return patterns with maximum frequency
    frequent_patterns = set()

    for pattern, count in frequency.items():
        if count == max_count:
            frequent_patterns.add(pattern)

    return frequent_patterns