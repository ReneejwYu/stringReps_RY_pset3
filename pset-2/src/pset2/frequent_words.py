#from frequent_words import FrequentWords as inclass_frequent_words


def frequentWords(text: str, k: int) -> set[str]:
    freqDic = {}
    for i in range(len(text)- k + 1):
        pattern = text[i:i+k]

        if pattern not in freqDic:
            freqDic[pattern] = 1
        else:
            freqDic[pattern] = +1
    
    max_count = max(freqDic.values())

    for pattern in freqDic:
        if freqDic[pattern] == max_count:
            return pattern

    raise NotImplementedError("Implement frequentWords")

