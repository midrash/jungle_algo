N = int(input())


def fact(a):
    if a == 0:
        return 1
    return fact(a - 1) * a


result = fact(N)
print(result)
