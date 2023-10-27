testCount = int(input())
word_list = []
new_word_list = []

#테스트 케이스 입력 리스트에 단어 붙이기
for _ in range(testCount) :
    word = input()
    word_list.append(word)

#중복되는 단어 제거
for word in word_list:
    if word not in new_word_list:
        new_word_list.append(word)

print(new_word_list)

#길이가 짧은 순서로 정렬, 길이가 같을 경우 사전순으로
#단어의 길이를 비교하고 그 후 길이가 같다면 단어 자체를 사전순으로 비교
sorted_list = sorted(new_word_list, key=lambda x: (len(x),x)) 

