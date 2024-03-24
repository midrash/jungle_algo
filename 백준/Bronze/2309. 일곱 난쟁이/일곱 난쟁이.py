arr = [int(input()) for _ in range(9)]
# N = int(input())
# arr = [sys.stdin.readlined().strip() for _ in range(N)]
result_arr = []
arr.sort()


def checknanjang(depth, start, sum, result):
    if depth == 7:
        if sum == 100:
            for i in result:
                print(i)
            exit()
        else:
            return
    for j in range(start, 9):
        result.append(arr[j])
        sum += arr[j]
        checknanjang(depth + 1, start + 1, sum, result)
        result.pop()
        sum -= arr[j]


checknanjang(0, 0, 0, result_arr)
