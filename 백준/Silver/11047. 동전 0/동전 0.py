import sys

#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, K = map(int, input().split())
coins = []
for _ in range(N):
    coin = int(input())
    coins.append(coin)
# print(N, K, coins)

result = 0
k = K
while k > 0:
    for i in range(N - 1, -1, -1):
        if k // coins[i] > 0:
            result += k // coins[i]
            k = k % coins[i]
            # print(f"result 증가함 {result}, 남은 금액 :{k}")
print(result)
