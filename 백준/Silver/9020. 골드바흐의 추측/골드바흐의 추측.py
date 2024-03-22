def checksosu(a):
    if a == 2:
        return True
    if a % 2 == 0:
        return False
    for i in range(2, a):
        if a % i == 0:
            return False
        if i >= a / 2:
            return True


T = int(input())
for i in range(T):
    num = int(input())
    a, b = num // 2, num // 2
    for j in range(1, num // 2):
        if checksosu(a) and checksosu(b):
            print(a, b)
            break
        else:
            a -= 1
            b += 1
