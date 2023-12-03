from frequency_map import FrequencyMap
from max_map import MaxMap
def FrequentWords(Text, k):
    words =[]
    freq = FrequencyMap(Text, k)
    m = MaxMap(freq)
    for key in freq:
        if freq[key] == m:
            words.append(key)
    return words
