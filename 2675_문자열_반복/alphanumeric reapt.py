T=int(input()) #테스트 케이스 갯수 저장 
for _ in range(T): 
    N, S=input().split() #숫자와 문자열을 저장 여기엔 \n도 포함되어 있다.
    for i in S: #문자열 요소를 돌면서 
        print(i*int(N), end="") #문자 요소에 N을 곱하고 end=""로 \n 방지
    print()