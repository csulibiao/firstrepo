# 1 <= a[i] <= n, a[i] will appear 1 or 2 times, find the missing number
# [3,4,6,3,2,1,6,8] -> [5,7]


def findMissing(nums):
    for i in range(len(nums)):
        index = abs(nums[i]) - 1
        nums[index] = -abs(nums[index])
    return [i + 1 for i in range(len(nums)) if nums[i] > 0]


print(findMissing([3, 4, 6, 3, 2, 1, 6, 8]))
