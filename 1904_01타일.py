# dp[n]은 길이가 n인 가능한 모든 2진 수열의 개수를 나타냄
# 초기조건 : d[1] = 1(1) dp[2] = 2(00, 11)
# 점화식 dp[n] = dp[n-1] + dp[n-2]

N = int(input())

dp = [0] * (N + 1)

dp[1] = 1
if N > 1:
    dp[2] = 2

for i in range(3, N + 1):
    dp[i] = (dp[i-1] + dp[i-2] % 15746)

print(dp[N])
