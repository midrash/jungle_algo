n = int(input())
nums = [int(input()) for _ in range(n)]
nums.sort()

for i in range(len(nums)):
    print(nums[i])