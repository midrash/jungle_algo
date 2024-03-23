N = int(input())


def hanoi(N, t1, t3, t2):
    if N == 1:
        print(t1, t3)
        return
    hanoi(N - 1, t1, t2, t3)
    print(t1, t3)
    hanoi(N - 1, t2, t3, t1)


print(2**N - 1)
if N <= 20:
    hanoi(N, 1, 3, 2)
