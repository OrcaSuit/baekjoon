# 입력: 첫 줄에는 수의 개수 N
N = int(input())

# 입력: N개의 수를 리스트에 저장
numbers = [int(input()) for _ in range(N)]

# 오름차순으로 정렬
sorted_numbers = sorted(numbers)

# 출력: 정렬된 결과를 한 줄에 하나씩 출력
for num in sorted_numbers:
    print(num)
