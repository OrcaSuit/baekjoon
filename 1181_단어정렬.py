import sys

count = int(sys.stdin.readline())
words = []

for _ in range(count):
    words.append(sys.stdin.readline().strip())

sorted_words = sorted(words, key=lambda x: (len(x), x)) #람다, 길이반환, 단어자체비교반환

unique_words = []
seen = set()

for sorted_word in sorted_words:
    if sorted_word not in seen:
        unique_words.append(sorted_word)
        seen.add(sorted_word)


for i in range(len(unique_words)):
    print(unique_words[i])

