num_list = [input() for _ in range(9)]
for i, val in enumerate(num_list):
    num_list[i] = int(val)
max = num_list[0]
order = 0
num = 0

for i, val in enumerate(num_list):
    if max < val:
        max = val
        num = i
print(max)
print(num + 1)
