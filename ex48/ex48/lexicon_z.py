lexicon = {
    "north": 'direction',
}

def scan(scentence):
    results = []
    words = scentence.split()
    for word in words:
        word_type = lexicon.get(word)
        results.append((word_type, word))
    return results