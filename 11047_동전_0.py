N, k = map(int, input().split())
coins = [int(input()) for _ in range(N)]

count = 0

for coin in reversed(coins):
    count += k // coin
    k %= coin
print(count)