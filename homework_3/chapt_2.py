import collections

def count_unique_words(text):
    word_count = collections.Counter([word.strip(",.?!") for word in text.lower().split()])
    return len([word for word, count in word_count.items()])

sentence = "Bananas are good, but bananas are even better! I love bananas."
print(count_unique_words(sentence))
