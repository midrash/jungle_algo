import sys
N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# for i in range(len(arr)):
#     print(arr[i])

checkarr = [False] * N
minpay = 99999999


def seller(start, now, checkarr, depth, pay):
    global minpay
    if pay > minpay:
        return
    # print(f"현재위치 :{now}, 간곳: {checkarr}, 지금깊이: {depth}, 지금까지비용: {pay}")

    if depth == N:
        # print(f"한바퀴 비용 {pay}")
        if pay < minpay:
            minpay = pay
            return
    else:
        for i in range(N):
            # print(
            #     f"현재위치 :{now} 다음 목적지 :{i}, 다음 목적지 비용: {arr[now][i]}, 방문 여부 :{checkarr[i]}"
            # )
            if arr[now][i] != 0:
                if depth == N - 1:
                    if checkarr[i] == False:
                        pay += arr[now][i]
                        depth += 1
                        checkarr[i] = True
                        seller(start, i, checkarr, depth, pay)
                        pay -= arr[now][i]
                        depth -= 1
                        checkarr[i] = False
                else:
                    if checkarr[i] == False and i != start:
                        pay += arr[now][i]
                        depth += 1
                        checkarr[i] = True
                        seller(start, i, checkarr, depth, pay)
                        pay -= arr[now][i]
                        depth -= 1
                        checkarr[i] = False


for i in range(N):
    seller(i, i, checkarr, 0, 0)

print(f"{minpay}")
