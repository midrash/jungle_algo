import sys

#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

T = int(input())


def greedy(N, arr):
    # visited = [1] * N
    result = 1
    max_ = arr[0][1]
    for i in range(1, N):
        # print(f"이번 기준 사원 서류: {arr[i][0]}등, 면접: {arr[i][1]}등")
        if max_ > arr[i][1]:
            result += 1
            max_ = arr[i][1]
    # print(f"남은 인원수: {result}")
    print(f"{result}")


for _ in range(T):
    N = int(input())
    arr = []
    for _ in range(N):
        a, b = map(int, input().split())
        arr.append((a, b))
    arr.sort()
    # print(arr)
    greedy(N, arr)

