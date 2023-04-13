def isSorted(nums):
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            return False
    return True

t = int(input())
for i in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    result = isSorted(nums)
    if result:
        print("Yes")
    else:
        print("No")
