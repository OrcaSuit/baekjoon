def repeat_string(R, S): #주어진 문자열 S의 각 문자를 R번 반복하여 새로운 문자열을 반환하는 기능
    result = ''
    for char in S:
        result += char * R
    return result

def main():
    #테스트 케이스의 개수 입력 받음
    T = int(input())

    for _ in range(T):

        R, S = input().split()
        R = int(R)

        print(repeat_string(R, S))

if __name__ == "__main__":
    main()