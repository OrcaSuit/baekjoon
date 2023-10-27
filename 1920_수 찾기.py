# 이진 검색 함수
def binary_search(array, target):
    start, end = 0, len(array) - 1
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return 1
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return 0

n = int(input())
A = list(map(int, input().split()))
A.sort()

m = int(input())
B = list(map(int, input().split()))

for num in B:
    print(binary_search(A, num))
