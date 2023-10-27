# 테스트 케이스의 개수 T를 입력 받음
T = int(input())

#각 테스트 케이스에 대해 작업을 수행
for _ in range(T):
    #반복 횟수 R과 문자열 S를 입력 받음
    R, S = input().split()
    R = int(R) # R를 정수로 변환

    # 출력할 문자열 P를 초기화
    P = ''

    # 문자열 S의 각 문자를 R번 반복하여 P에 추가
    for char in S:
        P += char * R
    print(P)