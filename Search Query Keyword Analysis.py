query = "Buy mobile phone buy phone online"
query = query.lower()
words = query.split()
frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1
result = {word: count for word, count in frequency.items() if count > 1}
print(result)