import sys

#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

T = int(input())
#print(f"테케 수 :{T}")


def make_coins(coins, M):
    # 코인 조합 수 배열 초기화
    arr = [0] * (M + 1)
    arr[0] = 1
    # print(f"코인 목록:{coins}, 목표 금액:{M}")
    for i in coins:
        for j in range(i, M + 1):
            # print(f"이번 코인: {i}, 이번 확인 금액 순서: {j}")
            arr[j] += arr[j - i]
    print(arr[M])


for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())
    make_coins(coins, M)